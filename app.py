from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'una-chiave-segreta-a-caso'  # Serve per sessioni sicure
colori = ['rosso', 'blu', 'verde', 'giallo', 'arancione', 'viola', 'rosa', 'marrone', 'nero', 'bianco', 'azzurro']
domande = [
    {
        "id": 1,
        "testo": "Il primo trofeo internazionale del Napoli è stata la Coppa UEFA vinta nel 1989.",
        "risposta_corretta": True
    },
    {
        "id": 2,
        "testo": " Dopo il fallimento nel 2004, il Napoli è stato rifondato come Napoli Soccer",
        "risposta_corretta": True
    },
    {
        "id": 3,
        "testo": "Il Napoli non ha mai disputato una finale di Champions League.",
        "risposta_corretta": True
    },
    {
        "id": 4,
        "testo": "Maradona arrivò al Napoli dal Barcellona nel 1984.",
        "risposta_corretta": True
    },
    {
        "id": 5,
        "testo": "Il secondo scudetto fu vinto nella stagione 1989/1990.",
        "risposta_corretta": True
    },
    {
        "id": 6,
        "testo": "Careca, Alemao e Maradona formavano il famoso trio “Ma-Gi-Ca”.",
        "risposta_corretta": True
    },
    {
        "id": 7,
        "testo": "Nel 2006 il Napoli giocava in Serie C1.",
        "risposta_corretta": True
    },
    {
        "id": 8,
        "testo": "Il Napoli debuttò in Serie A negli anni '60.",
        "risposta_corretta": True
    },
    {
        "id": 9,
        "testo": "Mazzarri portò il Napoli in Champions League nel 2011.",
        "risposta_corretta": True
    },
    {
        "id": 10,
        "testo": "Il Napoli vinse la Coppa Italia 2011/2012 battendo l’Inter in finale.",
        "risposta_corretta": False
    },
    {
        "id": 11,
        "testo": "Higuaín segnò 36 gol in Serie A nella stagione 2015/2016.",
        "risposta_corretta": True
    },
    {
        "id": 12,
        "testo": "Il Napoli non ha mai vinto la Coppa UEFA (oggi Europa League) nel 1990.",
        "risposta_corretta": False
    },
    {
        "id": 13,
        "testo": "Antonio Juliano fu storico capitano negli anni '70.",
        "risposta_corretta": True
    },
    {
        "id": 14,
        "testo": "Il Napoli assunse il nome Società Sportiva Calcio Napoli nel 1964.",
        "risposta_corretta": True
    },
    {
        "id": 15,
        "testo": "Il Napoli tornò in Serie A nel 2007 con Ventura.",
        "risposta_corretta": False
    },
    {
        "id": 16,
        "testo": "Il Napoli fu eliminato dall’Arsenal ai quarti di Europa League nel 2019.",
        "risposta_corretta": True
    },
    {
        "id": 17,
        "testo": "Il Napoli ha partecipato e vinto la Supercoppa Italiana contro l'Inter.",
        "risposta_corretta": False
    },
    {
        "id": 18,
        "testo": "Il Napoli vinse la Supercoppa Italiana nel 1990 contro la Juventus.",
        "risposta_corretta": True
    },
    {
        "id": 19,
        "testo": " Ciro Ferrara iniziò al Napoli ma terminò la carriera in altri club (Juventus).",
        "risposta_corretta": True
    },
    {
        "id": 20,
        "testo": "Nel 2017/2018 il Napoli fece 91 punti senza vincere lo scudetto.",
        "risposta_corretta": True
    },
    {
        "id": 21,
        "testo": "Prima partecipazione alla Champions League moderna nel 2011/2012.",
        "risposta_corretta": True
    },
    {
        "id": 22,
        "testo": "Dries Mertens è il miglior marcatore nella storia del Napoli.",
        "risposta_corretta": True
    },
    {
        "id": 23,
        "testo": "Zdeněk Zeman non è mai stato allenatore del Napoli.",
        "risposta_corretta": False
    },
    {
        "id": 24,
        "testo": "Il Napoli non ha mai vinto la Coppa delle Coppe.",
        "risposta_corretta": False
    },
    {
        "id": 25,
        "testo": "Napoli ha affrontato il Chelsea in Champions League.",
        "risposta_corretta": True
    },
    {
        "id": 26,
        "testo": " Nel 1987 il Napoli vinse lo scudetto ma non la Coppa Italia.",
        "risposta_corretta": False
    },
    {
        "id": 27,
        "testo": "Lavezzi, Higuaín e Mertens hanno giocato insieme nel Napoli.",
        "risposta_corretta": False
    },
    {
        "id": 28,
        "testo": "Napoli ha raggiunto la semifinale di Europa League contro il Villarreal nel 2015.",
        "risposta_corretta": False
    },
    {
        "id": 29,
        "testo": "Napoli ha vinto alcune partite ufficiali al Camp Nou contro il Barcellona (es. Europa League).",
        "risposta_corretta": False
    },
    {
        "id": 30,
        "testo": "Cannavaro esordì in Serie A con il Napoli, ma poi si trasferì presto altrove.",
        "risposta_corretta": True
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/numero', methods=['GET', 'POST'])
def numero():
    messaggio_vittoria = None

    if 'numero_da_indovinare' not in session:
        # Nuova partita
        session['numero_da_indovinare'] = random.randint(1, 100)
        session['numero_tentativi'] = 0

    tentativi = session.get('numero_tentativi', 0)
    numero_da_indovinare = session.get('numero_da_indovinare')
    messaggio = 'Indovina il numero da 1 a 100!'  # messaggio di default

    if request.method == 'POST':
        try:
            tentativo = int(request.form['tentativo'])
            # Controllo range 1-100
            if tentativo < 1 or tentativo > 100:
                messaggio = "Inserisci un numero compreso tra 1 e 100!"
            else:
                tentativi += 1
                session['numero_tentativi'] = tentativi

                if tentativo < numero_da_indovinare:
                    messaggio = "Più alto!"
                elif tentativo > numero_da_indovinare:
                    messaggio = "Più basso!"
                else:
                    messaggio_vittoria = f"Hai indovinato il numero in {tentativi} tentativi!"
                    # Reset sessione ma teniamo il messaggio di vittoria per questa richiesta
                    session.pop('numero_da_indovinare', None)
                    session.pop('numero_tentativi', None)
                    messaggio = 'Indovina il numero da 1 a 100!'  # nuova partita

                    # Subito nuova partita
                    session['numero_da_indovinare'] = random.randint(1, 100)
                    session['numero_tentativi'] = 0

        except ValueError:
            messaggio = "Inserisci un numero valido!"

    return render_template(
        'numero.html',
        messaggio=messaggio,
        tentativi=session.get('numero_tentativi', 0),
        messaggio_vittoria=messaggio_vittoria,
    )

@app.route('/colore', methods=['GET', 'POST'])
def colore():
    messaggio_vittoria = None

    if 'colore_da_indovinare' not in session or 'colori_sbagliati' not in session:
        session['colore_da_indovinare'] = random.choice(colori)
        session['colore_tentativi'] = 0
        session['colori_sbagliati'] = []  # inizializza lista colori sbagliati

    messaggio = session.get('messaggio', 'Indovina il colore!')
    tentativi = session.get('colore_tentativi', 0)

    if request.method == 'POST':
        tentativo = request.form.get('tentativo')
        if tentativo not in colori:
            messaggio = "Colore non valido!"
        else:
            tentativi += 1
            session['colore_tentativi'] = tentativi
            colore_da_indovinare = session['colore_da_indovinare']

            if tentativo == colore_da_indovinare:
                messaggio_vittoria = f"Hai indovinato il colore in {tentativi} tentativi!"
                session.pop('colore_da_indovinare', None)
                session.pop('colore_tentativi', None)
                session.pop('colori_sbagliati', None)
                messaggio = 'Indovina il colore!'

                # Nuova partita
                session['colore_da_indovinare'] = random.choice(colori)
                session['colore_tentativi'] = 0
                session['colori_sbagliati'] = []
            else:
                messaggio = "Sbagliato! Riprova."
                # Aggiungi alla lista dei colori sbagliati solo se non è già presente
                if tentativo not in session['colori_sbagliati']:
                    session['colori_sbagliati'].append(tentativo)

    # Rimuovi i colori sbagliati dalla lista da mostrare nel menu
    colori_disponibili = [c for c in colori if c not in session.get('colori_sbagliati', [])]

    return render_template(
        'colore.html',
        colori=colori_disponibili,
        messaggio=messaggio,
        tentativi=session.get('colore_tentativi', 0),
        messaggio_vittoria=messaggio_vittoria,
    )

@app.route('/prigioniero', methods=['GET', 'POST'])
def prigioniero():
    messaggio = None
    risultato = None

    # Inizializza nuova partita se mancano le chiavi
    if 'porte' not in session:
        session['porte'] = [
            {"nome": "A", "portaCorretta": False},
            {"nome": "B", "portaCorretta": False}
        ]
        session['guardiani'] = [
            {"nome": "Guardiano 1", "diceVerità": False},
            {"nome": "Guardiano 2", "diceVerità": False}
        ]
        session['porte'][random.randint(0, 1)]["portaCorretta"] = True
        session['guardiani'][random.randint(0, 1)]["diceVerità"] = True
        session.pop('risposta_guardiano', None)  # resetto risposta guardiano
        step = "scegli_guardiano"

    else:
        # Se la partita è già iniziata ma non è stata scelta la porta
        if 'risposta_guardiano' in session and not risultato:
            step = "scegli_porta"
        else:
            step = "scegli_guardiano"

    if request.method == 'POST':
        if 'scelta_guardiano' in request.form:
            scelta_guardiano = int(request.form['scelta_guardiano']) - 1
            guardiano = session['guardiani'][scelta_guardiano]
            porta_vera = "A" if session['porte'][0]["portaCorretta"] else "B"
            porta_falsa = "B" if porta_vera == "A" else "A"
            risposta = porta_vera if guardiano["diceVerità"] else porta_falsa
            session['risposta_guardiano'] = risposta
            messaggio = f"Il guardiano ti dice: 'La porta corretta è la {risposta}'"
            step = "scegli_porta"

        elif 'scelta_porta' in request.form:
            scelta = request.form['scelta_porta']
            porta_corretta = "A" if session['porte'][0]["portaCorretta"] else "B"
            if scelta == porta_corretta:
                risultato = "Hai scelto la porta della libertà! 🎉"
            else:
                risultato = "Oh no! Era la porta della morte. 💀"

            # Resetta la sessione
            session.pop('porte', None)
            session.pop('guardiani', None)
            session.pop('risposta_guardiano', None)

            # Ricrea la partita subito
            session['porte'] = [
                {"nome": "A", "portaCorretta": False},
                {"nome": "B", "portaCorretta": False}
            ]
            session['guardiani'] = [
                {"nome": "Guardiano 1", "diceVerità": False},
                {"nome": "Guardiano 2", "diceVerità": False}
            ]
            session['porte'][random.randint(0, 1)]["portaCorretta"] = True
            session['guardiani'][random.randint(0, 1)]["diceVerità"] = True

            # Dopo risultato, resetto passo alla scelta guardiano
            step = "scegli_guardiano"

    return render_template(
        'prigioniero.html',
        messaggio=messaggio,
        risposta_guardiano=session.get('risposta_guardiano'),
        risultato=risultato,
        step=step
    )

@app.route('/trueorfalse', methods=['GET', 'POST'])
def true_or_false():
    if 'indice' not in session:
        session['indice'] = 0
        session['punteggio'] = 0

    indice = session['indice']

    # quiz terminato
    if indice >= len(domande):
        punteggio_finale = session['punteggio']
        session.clear()
        return render_template('trueorfalse.html', punteggio=punteggio_finale, completato=True)

    domanda_corrente = domande[indice]

    if request.method == 'POST':
        risposta_utente = request.form.get('risposta')
        if risposta_utente:
            utente_bool = True if risposta_utente == 'vero' else False
            if utente_bool == domanda_corrente['risposta_corretta']:
                session['punteggio'] += 1
        session['indice'] += 1
        return redirect(url_for('true_or_false'))

    return render_template('trueorfalse.html', domanda=domanda_corrente, completato=False)


if __name__ == '__main__':
    app.run(debug=True)
