import subprocess

# Converts total and remaining capacity to percentage
def checkPower(Capacity, Remaining):
	return (Remaining/Capacity) * 100

# Checks whether the latop is connected to a power source or not.
chargerConnectionStat = subprocess.check_output('system_profiler SPPowerDataType | grep \"Connected:\" | awk \'{print $2}\'', shell=True).decode('ascii')

# Gets total battery capacity and converts it to an int
chargeCapacity = int(subprocess.check_output('system_profiler SPPowerDataType | grep \"Full Charge Capacity (mAh):\" | awk \'{print $5}\'', shell=True).decode('ascii'))


# Gets remaining battery capacity and converts it to an int
chargeRemaining = int(subprocess.check_output('system_profiler SPPowerDataType | grep \"Charge Remaining (mAh):\" | awk \'{print $4}\'', shell=True).decode('ascii'))


# Passes total and remaining capacity into percentage convertor function
batteryPercentage = int(checkPower(chargeCapacity, chargeRemaining))

# Checks whether the charge percentage is over 80 if the charger is connected
if chargerConnectionStat == "Yes\n" and batteryPercentage >= 78:
	subprocess.run('say Battery is charged, please disconnect', shell=True)


# If the former is not true, checks whether the charge is below 40 if the charger is not connected
elif chargerConnectionStat == "No\n" and batteryPercentage <= 40:
	subprocess.run('say Battery needs charging, please connect', shell=True)
