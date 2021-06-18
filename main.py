try:
    import matplotlib.pyplot as plt
    import pandas as pd
    from tkinter import Tk
    # from Tkinter import Tk     # from tkinter import Tk for Python 3.x
    from tkinter.filedialog import askopenfilename
except ImportError:
    print('Import Error: you need to run \'pip install matplotlib pandas numpy scipy\'')
    print('If this keeps failing, you probably need to install tkinter.')


Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

# Read csv or excel files
if filename.lower().endswith('csv'):
    print('Reading CSV as dataframe...')
    data = pd.read_csv(filename)
elif filename.lower().endswith(('xls', 'xlsb', 'xlsm', 'xlsx')):
    print('Reading Excel file')
    data = pd.read_excel(filename)
else:
    print("You did not select a valid file")
    exit(0)

# preview data
print(data.head())

# store column headers as a list
headers = [col for col in data.columns]
print(headers)

# you can manually set the beginning and end time for the range
time_begin = 0
time_end = None

try:
    time = data['time'][time_begin:time_end]
    x = data['x'][time_begin:time_end]
    y = data['y'][time_begin:time_end]
    z = data['z'][time_begin:time_end]
except Exception as e:
    print(f'There was an error with: {e}')

fig, axs = plt.subplots(3, sharex=True, sharey=True)
fig.suptitle('Title')

axs[0].title('x')
axs[0].xlabel('time (s)')
axs[0].ylabel('Force x')
axs[0].plot(time, x)


axs[1].title('y')
axs[1].xlabel('time (s)')
axs[1].ylabel('Force y')
axs[1].plot(time, y)

axs[2].title('z')
axs[2].xlabel('time (s)')
axs[2].ylabel('Force z')
axs[2].plot(time, z)

plt.show()