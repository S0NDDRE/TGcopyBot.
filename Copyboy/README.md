## Hurtigoppsett for Mac

Last ned ZIP-filen `TGCopyBot.zip`, pakk ut, og kjør:

```bash
chmod +x setup.sh
./setup.sh
```

Dette sjekker Python3, installerer avhengigheter automatisk, og guider deg videre. Ingen ekstra nedlastinger nødvendig!

Kjør deretter `python3 tg_copy_bot.py` – scriptet ber om API-nøkkel, hash, telefonnummer, gruppe-ID og kanal-ID hvis de ikke allerede er i .env. Det lagrer dem automatisk for neste gang.

## Metode 1: Lag din egen Python-bot (gratis, men krever litt teknisk kunnskap)

Denne metoden bruker biblioteket Telethon, som logger inn på din Telegram-konto og automatisk kopierer meldinger. Den fungerer selv om videresending er deaktivert, fordi den sender innholdet som en "ny" melding i din kanal. Trinnene er basert på en populær GitHub-veiledning.

### Trinn-for-trinn veiledning

1. **Installer Python:**
   - Last ned og installer Python fra python.org (versjon 3.10+). Velg "Add Python to PATH" under installasjonen.

2. **Last ned scriptet:**
   - Gå til GitHub-repoen: <https://github.com/redianmarku/Telegram-Autoforwarder>.
   - Klikk "Code" > "Download ZIP". Pakk ut filen til skrivebordet ditt (mappe: telegram-auto-forward-master).

3. **Åpne i en editor (valgfritt, men anbefalt):**
   - Installer Visual Studio Code (gratis fra code.visualstudio.com).
   - Åpne mappen i VS Code via "File > Open Folder".

4. **Installer nødvendige pakker:**
   - Åpne terminalen i VS Code (eller kommandolinjen på Windows/Mac).
   - Kjør: `pip install -r requirements.txt` (dette installerer Telethon og andre biblioteker).

5. **Få API-nøkler fra Telegram:**
   - Gå til my.telegram.org.
   - Logg inn med telefonnummeret ditt og bekreftelseskoden fra Telegram-appen.
   - Klikk "API development tools".
   - Opprett en ny app (fyll inn dummy-info som "App title: Test", "Short name: test").
   - Kopier API ID (tall) og API Hash (tekststreng).

6. **Kjør scriptet og logg inn:**
   - I terminalen, kjør: `python telegram_forward.py` (eller `python3 telegram_forward.py` på Mac/Linux).
   - Skriv inn API ID, API Hash og telefonnummeret ditt.
   - Skriv inn bekreftelseskoden fra Telegram-appen.

7. **Finn chat-ID-er:**
   - Velg "1. List chats" i menyen.
   - Scriptet lister alle dine chats/grupper/kanaler med ID-er (f.eks. -1001234567890 for kanaler – noter den negative ID-en).
   - ID-ene lagres i en fil hvis de ikke vises i terminalen.

8. **Konfigurer forwarding:**
   - Kjør scriptet igjen og velg "2. Forward messages".
   - Skriv inn kilde-ID (fra den begrensede kanalen du er medlem av).
   - Skriv inn mål-ID (din egen kanal – du må være admin der).
   - (Valgfritt) Legg til nøkkelord for filtrering, f.eks. salg,kjøp (kommaseparert) – la stå tomt for alle meldinger.

9. **Start og test:**
   - Scriptet overvåker nå kanalen. Send en testmelding i kildekanalen – den skal dukke opp i din kanal innen sekunder.
   - For å stoppe: Trykk Ctrl+C i terminalen.

### Eksempelkode (hoveddelen av scriptet)

Scriptet bruker Telethon til å lytte til nye meldinger og kopiere dem. Her er en forenklet versjon av kjernedelen (fra repoen – tilpass ID-ene):

```python
from telethon import TelegramClient, events

api_id = 'DIN_API_ID'
api_hash = 'DIN_API_HASH'
source_chat = -1001234567890  # Kilde-ID
target_chat = -1009876543210  # Mål-ID

client = TelegramClient('session', api_id, api_hash)

@client.on(events.NewMessage(chats=source_chat))
async def handler(event):
    await client.send_message(target_chat, event.message)

client.start()
client.run_until_disconnected()
```

- Lagre som forward.py, erstatt ID-ene, og kjør med `python forward.py`.

### Begrensninger for metode 1

- Fungerer bare hvis du er medlem i kildekanalen.
- Krever at datamaskinen din kjører scriptet kontinuerlig (bruk en VPS som Heroku eller Raspberry Pi for 24/7).
- For media (bilder/video): Scriptet laster ned og laster opp automatisk, men det tar litt tid.

## Metode 2: Bruk en ferdig tjeneste (enkelt, men betalt)

Hvis du ikke vil kode, bruk Redirect Bot – en bot-tjeneste som håndterer kopiering automatisk og omgår restriksjoner ved å sende som nye meldinger.

### Trinn-for-trinn

1. Gå til <redirect-bot.com> og opprett en konto (gratis trial).

2. For privat kanal uten invitasjonslenke (krever PRO-plan, ca. 5–10 USD/mnd):
   - Koble din Telegram-konto i "Accounts"-seksjonen.
   - Opprett et nytt prosjekt i "My Projects".
   - I "Connect Chats", velg kildekanalen som "Sender" (den vises hvis kontoen din er medlem).
   - Legg til din kanal som "Recipient" (du må være admin).
   - Konfigurer: Velg "alle meldinger", "etter nøkkelord" eller "fra spesifikke brukere".

3. For kanal med invitasjonslenke (gratis basis):
   - Opprett prosjekt og gå til "Connect Chats > Sender".
   - Lim inn invitasjonslenken – boten blir medlem.
   - Legg til mottaker og konfigurer som over.

4. Start forwarding – det skjer automatisk uten at du trenger å holde noe åpent.

### Begrensninger for metode 2

- PRO-plan nødvendig for personlig konto-kobling (for å unngå CAPTCHA-problemer).
- Risiko for suspensjon hvis Telegram oppdager det.
- Respekter etikk: Ikke del sensitiv info uten tillatelse.

## Tips og feilsøking

- Hvis det ikke fungerer: Sjekk at du har admin-rettigheter i målkanalen, og at API-nøklene er korrekte. For feil, se Telegrams feilmeldinger.
- 24/7-drift: Bruk en sky-tjeneste som Google Colab (gratis, men midlertidig) eller en VPS.
- Alternativer: Sjekk andre GitHub-repos som PetroVoronov/telegram-forward-user-bot for Node.js-versjon, eller søk etter "Telethon forward script" for oppdateringer.
- Oppdateringer: Telegram endrer API-en ofte – test alltid på en testkonto først.

Hvis du trenger hjelp med spesifikke feil eller kodejusteringer, gi mer detaljer!
