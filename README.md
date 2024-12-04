# PrinterMasterBot

PrinterMasterBot is a Telegram bot that allows users to send documents or photos directly to a connected printer. It integrates with the CUPS (Common Unix Printing System) to manage print jobs and supports deployment as a system service or Docker container.

---

## Features

- Accepts files or photos via Telegram and sends them to a connected printer.
- Configurable via environment variables for access control and bot token.
- Supports USB-connected printers with CUPS integration.
- Flexible deployment: run as a system service or as a Docker container.

---

## Installation Options

### Option 1: Run as a System Service

#### Prerequisites

1. **Install Required Software**:
   ```bash
   sudo apt-get install hplip cups
   ```
2. **Configure Your Printer**:
   - Open the CUPS web interface (`http://localhost:631`).
   - Add your printer and enable sharing for network printing.
3. **Install Python and Pipenv**:
   ```bash
   sudo apt-get install python3 pipenv
   ```

#### Steps

1. Clone the repository and navigate to the project directory:
   ```bash
   git clone https://github.com/your-repo/printermasterbot.git
   cd printermasterbot
   ```

2. Install Python dependencies:
   ```bash
   pipenv install
   ```

3. Configure the environment variables:
   - Edit the service file `printermasterbot.service` and add your `TOKEN` and `ALLOWED_USERNAMES` environment variables.

4. Install and enable the service:
   ```bash
   sudo cp printermasterbot.service /etc/systemd/system/
   sudo systemctl daemon-reload
   sudo systemctl enable printermasterbot.service
   sudo systemctl start printermasterbot.service
   ```

---

### Option 2: Run as a Docker Container

#### Prerequisites

- **Install Docker**:
  ```bash
  sudo apt-get install docker docker-compose
  ```

- Ensure your printer is configured with CUPS.

#### Build and Run with Docker

1. **Build the Docker Image**:
   ```bash
   docker build -t printermasterbot .
   ```

2. **Run the Docker Container**:
   ```bash
   docker run -it --name printermasterbot \
     --device=/dev/usb/lp0 \
     -v /var/run/cups/cups.sock:/var/run/cups/cups.sock \
     -e TOKEN=123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZ \
     -e ALLOWED_USERNAMES=user1,user2,user3 \
     printermasterbot
   ```

#### Using Docker Compose

1. Create a `docker-compose.yml` file:
   ```yaml
   version: "3.8"
   services:
     printermasterbot:
       image: printermasterbot
       container_name: printermasterbot
       restart: always
       devices:
         - /dev/usb/lp0:/dev/usb/lp0
       volumes:
         - /var/run/cups/cups.sock:/var/run/cups/cups.sock
       environment:
         - TOKEN=123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZ
         - ALLOWED_USERNAMES=user1,user2,user3
   ```

2. Start the container:
   ```bash
   docker-compose up -d
   ```

---

## Usage

1. Find the bot on Telegram by searching for `@your_bot_username`.
2. Start the bot with the `/start` command.
3. Send a document or photo to the bot, and it will send it to the printer.
4. Use the `/clean` command (restricted to allowed users) to clear old files.

---

## Environment Variables

- **`TOKEN`**: (Required) Your Telegram Bot API token.
  - Example: `123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZ`

- **`ALLOWED_USERNAMES`**: (Optional) A comma-separated list of Telegram usernames allowed to use the bot. If unset, all users can interact with the bot.
  - Example: `user1,user2,user3`

---

## Notes

- Ensure your printer is powered on and connected before starting the bot.
- For Docker deployments, make sure to forward USB devices and CUPS sockets to the container.
- The bot uses the `lp` command to send files to the printer with options like `fit-to-page` and `A4` media.

---

## Troubleshooting

- **Printer not detected**: Check CUPS configuration and ensure the printer is added and shared.
- **Bot not responding**: Verify your Telegram Bot API token and network connection.
- **Permission issues**: Ensure the user running the bot has access to the printer and CUPS.

Contributions and issues are welcome to improve PrinterMasterBot!
