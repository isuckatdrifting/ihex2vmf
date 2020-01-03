import argparse
import sys
class IHEX:
  def __init__(self):
    self.byte_count = 0
    self.line_cnt = 0
    self.blob = []
  
  def read_blob(self, ihex):
    # read all lines into blob
    print(">> Start converting from ihex to vmf for simulation")
    line_cnt = 0
    with open(ihex) as fp:
      line = fp.readline()
      while line:
        self.blob.append(line)
        line = fp.readline()
        line_cnt += 1
    print(">> Read " + str(line_cnt) + " lines")
    fp.close()

  def to_vmf(self, vmf):
    # convert each line in blob to vmf format
    with open(vmf, 'w') as fp:
      for i in range(0, len(self.blob)):
        # detect byte_count, start_address, type, and blob content in a blob_line
        blob_line = self.blob[i][1:].strip('\n') # remove the initial ':' and the end '\n'
        # print(blob_line)
        byte_count = int(blob_line[0:2], 16) # [0:1] in hex
        start_address = blob_line[2:6] # [2:5] in hex
        blob_type = int(blob_line[6:8], 16) # [6:7] in hex
        blob_content = blob_line[8:8+byte_count*2]
        # print(byte_count, start_address, blob_type, blob_content)
        if blob_type == 0:
          fp.write("@" + start_address + "\n")
          for j in range(0, byte_count):
            fp.write(blob_content[j*2:j*2+2] + "\n")
        elif blob_type == 3:
          print(">> Code Segment, Program Counter: " + blob_content)
    print(">> Conversion finished")
    fp.close()
      

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("input_hex", help="directory to hex file", type=str)
  parser.add_argument("output_vmf", help="directory to vmf file", type=str)
  args = parser.parse_args()
  ihex = IHEX()
  ihex.read_blob(args.input_hex)
  ihex.to_vmf(args.output_vmf)

