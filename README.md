# Sturmico
your friendly illegal horse gambling wager printing REST API for the Epson TM-T88III.

## Setup
Clone this repository and navigate into the folder
```bash
git clone https://github.com/schnea/sturmico.git
cd sturmico
```

Install all dependencies with `uv` (https://docs.astral.sh/uv/):
```bash
uv sync
```

Find your serial printer port with
```bash
ls /dev/ttyUSB*
```
and make sure you have the permissions to access it. You can either grant the permissions temporarily
```bash
sudo chmod a+rw /dev/ttyUSB0
```
or, as a more persistent approach, add your user to dialout:
```bash
sudo usermod -aG dialout $USER
```

run the development server with:
```bash
uv run fastapi dev main.py
```

## Usage
The API has only two endpoints: 
`curl http://localhost:8000/health`
to check if the server itself is running, and the actual printing endpoint: 

`curl http://localhost:8000/print/<number>/<horse>/<amount>`, e.g.
`curl http://localhost:8000/print/2/Marocco/5000`
