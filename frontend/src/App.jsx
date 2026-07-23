import { useEffect, useState } from 'react'
import './App.css'

const API_URL = 'http://127.0.0.1:8000/api/reforma/itens/'

const STATUS_OPTIONS = [
  { value: 'planejamento', label: 'Planejamento' },
  { value: 'em_andamento', label: 'Em andamento' },
  { value: 'concluido', label: 'Concluído' },
]

const CAMPOS_VAZIOS = {
  nome: '',
  categoria: '',
  custo_estimado: '',
  custo_real: '',
  status: 'planejamento',
  prioridade: '',
  data_estimavel: '',
}

function formatarMoeda(valor) {
  const numero = Number(valor)
  if (Number.isNaN(numero)) return valor
  return numero.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })
}

function formatarData(valor) {
  if (!valor) return '—'
  const [ano, mes, dia] = valor.split('-')
  return `${dia}/${mes}/${ano}`
}

function codigoItem(index) {
  return `R-${String(index + 1).padStart(3, '0')}`
}

function Prioridade({ valor }) {
  return (
    <span className="priority" aria-label={`Prioridade ${valor} de 5`}>
      {[1, 2, 3, 4, 5].map((n) => (
        <i key={n} className={n <= valor ? 'on' : ''} />
      ))}
    </span>
  )
}

function App() {
  const [itens, setItens] = useState([])
  const [form, setForm] = useState(CAMPOS_VAZIOS)
  const [erro, setErro] = useState(null)
  const [carregado, setCarregado] = useState(false)

  function carregarItens() {
    fetch(API_URL)
      .then((res) => res.json())
      .then((dados) => {
        setItens(dados)
        setCarregado(true)
      })
      .catch(() => setErro('Não foi possível conectar ao servidor Django. Confira se o backend está rodando na porta 8000.'))
  }

  useEffect(() => {
    carregarItens()
  }, [])

  function handleChange(event) {
    const { name, value } = event.target
    setForm((prev) => ({ ...prev, [name]: value }))
  }

  function handleSubmit(event) {
    event.preventDefault()
    setErro(null)

    fetch(API_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form),
    })
      .then((res) => {
        if (!res.ok) throw new Error('Erro ao salvar')
        return res.json()
      })
      .then(() => {
        setForm(CAMPOS_VAZIOS)
        carregarItens()
      })
      .catch(() => setErro('Não foi possível salvar o item. Revise os campos e tente novamente.'))
  }

  const concluidos = itens.filter((i) => i.status === 'concluido').length
  const totalEstimado = itens.reduce((soma, i) => soma + Number(i.custo_estimado || 0), 0)

  return (
    <div className="app">
      <header className="page-hero">
        <div className="page-hero-inner">
          <a className="back-link" href="http://127.0.0.1:8000/">← Organização Casamento</a>
          <p className="page-eyebrow">Módulo M-02</p>
          <h1>Reforma</h1>

          <div className="hero-stats">
            <div>
              <strong>{itens.length}</strong>
              <span>Itens cadastrados</span>
            </div>
            <div>
              <strong>{concluidos}</strong>
              <span>Concluídos</span>
            </div>
            <div>
              <strong>{formatarMoeda(totalEstimado)}</strong>
              <span>Custo estimado total</span>
            </div>
          </div>
        </div>
      </header>

      <section className="section-itens">
        <div className="section-head">
          <p className="section-eyebrow">Itens</p>
          <h2>O que está em obra</h2>
        </div>

        {erro && <p className="erro">{erro}</p>}

        {carregado && itens.length === 0 && !erro ? (
          <p className="aviso">
            Nenhum item registrado — comece adicionando o primeiro item abaixo.
          </p>
        ) : (
          <div className="grid-itens">
            {itens.map((item, index) => (
              <article className="card-item" key={item.id}>
                <p className="card-code">{codigoItem(index)}</p>
                <h3>{item.nome}</h3>
                <p className="card-meta">
                  <span>{item.categoria}</span>
                  <span>{formatarMoeda(item.custo_estimado)} est.</span>
                  <span>{formatarMoeda(item.custo_real)} real</span>
                </p>
                <Prioridade valor={item.prioridade} />
                <div className="card-footer">
                  <span className="badge" data-status={item.status}>
                    {STATUS_OPTIONS.find((s) => s.value === item.status)?.label}
                  </span>
                  <span className="card-date">{formatarData(item.data_estimavel)}</span>
                </div>
              </article>
            ))}
          </div>
        )}
      </section>

      <section className="section-novo">
        <div className="form-card">
          <h2>Novo item</h2>
          <form className="campos" onSubmit={handleSubmit}>
            <div className="campo full">
              <label htmlFor="nome">Nome</label>
              <input id="nome" name="nome" value={form.nome} onChange={handleChange} required />
            </div>

            <div className="campo full">
              <label htmlFor="categoria">Categoria</label>
              <input id="categoria" name="categoria" value={form.categoria} onChange={handleChange} required />
            </div>

            <div className="campo">
              <label htmlFor="custo_estimado">Custo estimado</label>
              <input
                id="custo_estimado"
                type="number"
                step="0.01"
                name="custo_estimado"
                value={form.custo_estimado}
                onChange={handleChange}
                required
              />
            </div>

            <div className="campo">
              <label htmlFor="custo_real">Custo real</label>
              <input
                id="custo_real"
                type="number"
                step="0.01"
                name="custo_real"
                value={form.custo_real}
                onChange={handleChange}
                required
              />
            </div>

            <div className="campo">
              <label htmlFor="status">Status</label>
              <select id="status" name="status" value={form.status} onChange={handleChange}>
                {STATUS_OPTIONS.map((opt) => (
                  <option key={opt.value} value={opt.value}>
                    {opt.label}
                  </option>
                ))}
              </select>
            </div>

            <div className="campo">
              <label htmlFor="prioridade">Prioridade (1 a 5)</label>
              <input
                id="prioridade"
                type="number"
                min="1"
                max="5"
                name="prioridade"
                value={form.prioridade}
                onChange={handleChange}
                required
              />
            </div>

            <div className="campo full">
              <label htmlFor="data_estimavel">Data estimável</label>
              <input
                id="data_estimavel"
                type="date"
                name="data_estimavel"
                value={form.data_estimavel}
                onChange={handleChange}
                required
              />
            </div>

            <button className="enviar" type="submit">Salvar item</button>
          </form>
        </div>
      </section>
    </div>
  )
}

export default App
