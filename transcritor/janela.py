# -*- coding: utf-8 -*-
"""Janelinha simples: cole os links, clique no botao, veja o andamento."""

import queue
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

import transcrever as nucleo


def abrir_janela(cfg):
    janela = tk.Tk()
    janela.title("Transcritor de video")
    janela.geometry("760x600")

    fila = queue.Queue()
    rodando = threading.Event()

    tk.Label(
        janela,
        text="Cole aqui os links (Instagram, TikTok ou YouTube), um por linha:",
        anchor="w",
    ).pack(fill="x", padx=12, pady=(12, 4))

    caixa_links = tk.Text(janela, height=7, wrap="word")
    caixa_links.pack(fill="x", padx=12)

    barra = tk.Frame(janela)
    barra.pack(fill="x", padx=12, pady=10)

    tk.Label(barra, text="Qualidade:").pack(side="left")
    escolha_modelo = ttk.Combobox(
        barra,
        values=["small", "medium", "large-v3"],
        width=10,
        state="readonly",
    )
    escolha_modelo.set(cfg["modelo"])
    escolha_modelo.pack(side="left", padx=(4, 16))

    var_pasta = tk.StringVar(value=cfg["pasta_saida"])

    def escolher_pasta():
        escolhida = filedialog.askdirectory(initialdir=var_pasta.get())
        if escolhida:
            var_pasta.set(escolhida)

    tk.Button(barra, text="Pasta de saida...", command=escolher_pasta).pack(
        side="left"
    )
    tk.Label(barra, textvariable=var_pasta, fg="#555").pack(
        side="left", padx=8
    )

    caixa_log = tk.Text(janela, wrap="word", state="disabled", bg="#f6f6f6")
    caixa_log.pack(fill="both", expand=True, padx=12, pady=(0, 8))

    def escrever(linha):
        fila.put(str(linha))

    def drenar():
        while True:
            try:
                linha = fila.get_nowait()
            except queue.Empty:
                break
            caixa_log.configure(state="normal")
            caixa_log.insert("end", linha + "\n")
            caixa_log.see("end")
            caixa_log.configure(state="disabled")
        janela.after(120, drenar)

    def trabalhar(links, config):
        try:
            nucleo.rodar(links, config, log=escrever)
        except Exception as e:
            escrever(f"ERRO GERAL: {e}")
        finally:
            rodando.clear()
            fila.put("")
            janela.after(0, lambda: botao.configure(
                state="normal", text="Transcrever"
            ))

    def comecar():
        if rodando.is_set():
            return
        links = nucleo.extrair_links(caixa_links.get("1.0", "end"))
        if not links:
            messagebox.showwarning(
                "Sem links", "Cole pelo menos um link antes de transcrever."
            )
            return
        config = dict(cfg)
        config["modelo"] = escolha_modelo.get()
        config["pasta_saida"] = var_pasta.get()
        nucleo.salvar_config(config)

        rodando.set()
        botao.configure(state="disabled", text="Transcrevendo...")
        escrever(f"{len(links)} link(s) para processar.")
        threading.Thread(
            target=trabalhar, args=(links, config), daemon=True
        ).start()

    botao = tk.Button(
        janela, text="Transcrever", command=comecar, height=2,
        bg="#2d6cdf", fg="white",
    )
    botao.pack(fill="x", padx=12, pady=(0, 12))

    janela.after(120, drenar)
    janela.mainloop()
