import React, { useState } from 'react';

// Vertalings-kluis
const translations = {
  af: {
    title: "Bybelstudie-Assistent",
    subtitle: "Deur Dr. Jan de Beer",
    placeholder: "Tik jou Bybelvraag hier...",
    button: "Ontleed Teks",
    switch: "Switch to English",
    loading: "Besig om na te dink...",
  },
  en: {
    title: "Bible Study Assistant",
    subtitle: "By Dr. Jan de Beer",
    placeholder: "Type your Bible question here...",
    button: "Analyze Text",
    switch: "Skakel na Afrikaans",
    loading: "Thinking...",
  }
};

export default function App() {
  const [language, setLanguage] = useState<'af' | 'en'>('af');
  const [input, setInput] = useState('');
  const [response, setResponse] = useState('');

  const t = translations[language];

  const handleAsk = () => {
    setResponse(t.loading);
    // Hierdie sal later met die regte KI-skakel werk
    setTimeout(() => setResponse(language === 'af' ? "Die Assistent is gereed vir jou vrae." : "The Assistant is ready for your questions."), 1000);
  };

  return (
    <div style={{ 
      padding: '40px', 
      fontFamily: 'Segoe UI, Tahoma, Geneva, Verdana, sans-serif',
      maxWidth: '800px',
      margin: '0 auto',
      backgroundColor: '#ffffff',
      minHeight: '100vh'
    }}>
      <header style={{ 
        display: 'flex', 
        justifyContent: 'space-between', 
        alignItems: 'center',
        borderBottom: '2px solid #2ecc71',
        paddingBottom: '20px'
      }}>
        <div>
          <h1 style={{ color: '#2ecc71', margin: 0, fontSize: '2.5rem' }}>{t.title}</h1>
          <p style={{ margin: '5px 0', color: '#666', fontStyle: 'italic' }}>{t.subtitle}</p>
        </div>
        <button 
          onClick={() => setLanguage(language === 'af' ? 'en' : 'af')}
          style={{ 
            padding: '10px 20px', 
            cursor: 'pointer', 
            borderRadius: '25px', 
            border: '2px solid #2ecc71',
            backgroundColor: 'transparent',
            color: '#2ecc71',
            fontWeight: 'bold',
            transition: '0.3s'
          }}
        >
          {t.switch}
        </button>
      </header>

      <main style={{ marginTop: '40px' }}>
        <textarea
          style={{ 
            width: '100%', 
            height: '180px', 
            padding: '20px', 
            borderRadius: '12px', 
            border: '1px solid #ddd',
            fontSize: '1.1rem',
            boxSizing: 'border-box',
            boxShadow: 'inset 0 2px 4px rgba(0,0,0,0.05)'
          }}
          placeholder={t.placeholder}
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />
        <button 
          onClick={handleAsk}
          style={{ 
            marginTop: '20px', 
            padding: '15px 40px', 
            backgroundColor: '#2ecc71', 
            color: 'white', 
            border: 'none', 
            borderRadius: '8px', 
            cursor: 'pointer', 
            fontWeight: 'bold',
            fontSize: '1.1rem',
            boxShadow: '0 4px 6px rgba(46, 204, 113, 0.3)'
          }}
        >
          {t.button}
        </button>

        {response && (
          <div style={{ 
            marginTop: '40px', 
            padding: '25px', 
            backgroundColor: '#f1fcf5', 
            borderRadius: '12px', 
            borderLeft: '8px solid #2ecc71',
            fontSize: '1.2rem',
            lineHeight: '1.6',
            color: '#2c3e50'
          }}>
            {response}
          </div>
        )}
      </main>
    </div>
  );
}