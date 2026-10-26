with open('text.txt','w') as f:
  f.write('hosdofio osadfo osoaddsfifj oofsdjai\n')
  f.write('hosdofsdsffio osdfssadfo osoadifj oofsdjai\n')
  f.write('hosdofio osadfo osoadifj oofsdjai\n')
  f.write('hosdofio osadfo osodfsadifsf sj oofsdjai\n')
  f.write('hosdofio osadfo osoadifj oofsdjai\n')
  f.write('hosdofio osadfo osoadifj oofsdjai\n')
  f.write('hossdfdofio osadfo osoadidsffj oofsdjai\n')
  f.write('hosdofio osadfo osoadifj oofsdjai\n')
  f.write('hosdofio osadfo sfosoadifj oofsdjai\n')
  f.write('hosdofio osadfo osoadifj oofsdjai\n')
with open('text.txt','r') as f:
  data=f.readlines()
print(len(data))
with open('new.txt','w') as f:
  f.writelines(data[:0])
print("done")
  