import React, {useEffect, useState} from 'react';
const API = '/api';

function App() {
  const [records,setRecords] = useState([]);
  const [types,setTypes] = useState([]);
  const [statuses,setStatuses] = useState([]);
  const [categories,setCategories] = useState([]);
  const [subcategories,setSubcategories] = useState([]);
  const [filters,setFilters] = useState({page:1, page_size:10, date_from:'', date_to:'', type:'', status:'', category:'', subcategory:''});
  const [form,setForm] = useState({date:'', status:'', type:'', category:'', subcategory:'', amount:'', comment:''});

  useEffect(()=>{
    fetchData();
    fetch(API+'/types/').then(r=>r.json()).then(setTypes);
    fetch(API+'/statuses/').then(r=>r.json()).then(setStatuses);
    fetch(API+'/categories/').then(r=>r.json()).then(setCategories);
    fetch(API+'/subcategories/').then(r=>r.json()).then(setSubcategories);
  },[]);

  function fetchData(){
    const params = new URLSearchParams();
    Object.entries(filters).forEach(([k,v])=>{ if(v) params.set(k,v); });
    fetch(API+'/records/?'+params.toString()).then(r=>r.json()).then(setRecords);
  }

  function onFilterChange(e){ setFilters(prev=>({...prev,[e.target.name]: e.target.value})); }
  function applyFilters(){ fetchData(); }

  function onChange(e){
    const {name,value} = e.target;
    setForm(prev=>({...prev,[name]:value}));
    if(name==='type'){ setForm(prev=>({...prev, category:'', subcategory:''})); }
    if(name==='category'){ setForm(prev=>({...prev, subcategory:''})); }
  }

  function submit(e) {
    e.preventDefault();
    const payload = {...form, amount: parseFloat(form.amount || 0)};
    if(!payload.date) delete payload.date;
    fetch(API+'/records/', {
      method:'POST',
      headers:{'Content-Type':'application/json'},
      body: JSON.stringify(payload)
    }).then(async r=>{
      if(!r.ok){
        alert('Ошибка '+r.status);
        const err=await r.json();
        console.error(err);
        return;
      }
      const data = await r.json();
      setRecords(prev=>[data,...prev]);
      setForm({date:'', status:'', type:'', category:'', subcategory:'', amount:'', comment:''});
    });
  }

  async function remove(id){
    if(!confirm('Удалить запись?')) return;
    const r = await fetch(API+'/records/'+id+'/',{method:'DELETE'});
    if(r.ok) setRecords(prev=>prev.filter(x=>x.id!==id));
  }

  return (
    <div>
      <h1>ДДС — Управление движением денежных средств</h1>

      <div className="controls">
        <input type="date" name="date_from" value={filters.date_from} onChange={onFilterChange} /> -
        <input type="date" name="date_to" value={filters.date_to} onChange={onFilterChange} />
        <select name="type" value={filters.type} onChange={onFilterChange}>
          <option value="">Все типы</option>
          {types.map(t=><option key={t.id} value={t.id}>{t.name}</option>)}
        </select>
        <select name="category" value={filters.category} onChange={onFilterChange}>
          <option value="">Все категории</option>
          {categories.map(c=><option key={c.id} value={c.id}>{c.name}</option>)}
        </select>
        <button className="btn" onClick={applyFilters}>Применить</button>
      </div>

      <form onSubmit={submit} style={{marginBottom:20}}>
        <input type="date" name="date" value={form.date} onChange={onChange} /> &nbsp;
        <select name="status" value={form.status} onChange={onChange}>
          <option value="">Статус</option>
          {statuses.map(s=><option key={s.id} value={s.id}>{s.name}</option>)}
        </select> &nbsp;
        <select name="type" value={form.type} onChange={onChange}>
          <option value="">Тип</option>
          {types.map(t=><option key={t.id} value={t.id}>{t.name}</option>)}
        </select> &nbsp;
        <select name="category" value={form.category} onChange={onChange}>
          <option value="">Категория</option>
          {categories.filter(c=>!form.type || c.type===parseInt(form.type)).map(c=><option key={c.id} value={c.id}>{c.name}</option>)}
        </select> &nbsp;
        <select name="subcategory" value={form.subcategory} onChange={onChange}>
          <option value="">Подкатегория</option>
          {subcategories.filter(s=>!form.category || s.category===parseInt(form.category)).map(s=><option key={s.id} value={s.id}>{s.name}</option>)}
        </select> &nbsp;
        <input name="amount" value={form.amount} onChange={onChange} placeholder="Сумма" /> &nbsp;
        <input name="comment" value={form.comment} onChange={onChange} placeholder="Комментарий" /> &nbsp;
        <button className="btn" type="submit">Добавить</button>
      </form>

      <table>
        <thead>
          <tr>
            <th>Дата</th>
            <th>Статус</th>
            <th>Тип</th>
            <th>Категория</th>
            <th>Подкатегория</th>
            <th>Сумма</th>
            <th>Комментарий</th>
            <th>Действия</th>
          </tr>
        </thead>
        <tbody>
          {records.map(r=>(
            <tr key={r.id}>
              <td>{r.date}</td>
              <td>{r.status_name}</td>
              <td>{r.type_name}</td>
              <td>{r.category_name}</td>
              <td>{r.subcategory_name}</td>
              <td>{r.amount}</td>
              <td>{r.comment}</td>
              <td>
                <button className="btn" onClick={()=>remove(r.id)}>Удалить</button>
                &nbsp;
                <a className="btn" href={`/admin/dds_app/record/${r.id}/change/`} target="_blank" rel="noopener noreferrer">
                  Редактировать
                </a>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
