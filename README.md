# Plot CSV

This will let you select a file to plot.

## Installation

Be sure to install the latest version of Python 3 along with Tkinter. Tkinter should be installed by default in Windows. It is installed separately in Linux.


Open powershell and cd to this directory and run the following commands:
```powershell
python3 -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
```

## Running

In powershell, run the following:
```powershell
python main.py
```

## Modify the Code

You will need to modify the code for your needs.

This is where you will need to modify the column names to match the csv and the time window you are looking at the data.
For instance, if the column name is `time(s)`, then change `time = data['time(s)'][time_begin:time_end]`

You can also change the beginning and ending time. NOTE: this is the index, not the actual timestamp.

```python
time_begin = 0
time_end = None

time = data['time'][time_begin:time_end]
x = data['x'][time_begin:time_end]
y = data['y'][time_begin:time_end]
z = data['z'][time_begin:time_end]
```

