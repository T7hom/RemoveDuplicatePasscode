#remove duplicate passcode
import hashlib

#files path
input_file_path = "int.txt"
output_file_path = "out.txt"

#setup hash
completed_lines_hash = set()

#open file
input_file = open(input_file_path, "r")
output_file = open(output_file_path, "w")

#check loop
for line in input_file:
  #check hash
  hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
  #check dupliacte
  if hashValue not in completed_lines_hash:
    output_file.write(line)
    completed_lines_hash.add(hashValue)
#close files
output_file.close()
input_file.close()