import argparse
import os

def utf8len(s):
    return len(s.encode('utf-8'))


def chunk_to_write(file, nb, ml):
    #If number of bytes is odd -2, else readlines method rounds up
    if (nb % 2) != 0:
        nb -= 2
    chunk_based_on_bytes = file.readlines(nb)
    chunk_based_on_lines = chunk_based_on_bytes[:ml]
    return chunk_based_on_lines

def create_filename(i_file, o_dir, f_name_part):
    file_name, file_extension = os.path.splitext(i_file)
    file_size = os.path.getsize(i_file)
    complete_output_name = os.path.join(o_dir, i_file+"-part"+str(f_name_part)+file_extension)
    if not os.path.isdir(o_dir):
        os.mkdir(o_dir)
    return complete_output_name

def write_to_file(chunk, f_name, t_bytes, o_dir, f_name_part):

    # complete_output_name = os.path.join(o_dir, f_name+"-part"+str(f_name_part)+f_extension)
    # if not os.path.isdir(o_dir):
    #     os.mkdir(o_dir)
    complete_output_name = create_filename(f_name, o_dir, f_name_part)

    o = open(complete_output_name,'w')
    for c in range(0,len(chunk)):
        t_bytes += utf8len(chunk[c])
        o.write(chunk[c])
    o.close()

    f_name_part += 1

    return t_bytes, f_name_part
    
def run_pipeline(input, file_part, m_mbytes, m_lines, t_bytes, o_dir):
    f = open(input,'r')
    
    # On next iteration, start at byte position we wrote to. 
    if file_part != 1:
        discard = f.readlines(t_bytes -2)

    chunk = chunk_to_write(f, m_mbytes, m_lines)
    total_bytes, file_part_returned = write_to_file(chunk, input, t_bytes, o_dir, file_part)

    return total_bytes, file_part_returned

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-file', type=str, required=True)
    parser.add_argument('--output-dir', type=str, required=True)
    parser.add_argument('--max-megabytes', type=int, required=True)
    parser.add_argument('--max-lines', type=int, required=True)

    args = parser.parse_args()


    input_file = args.input_file
    output_dir = args.output_dir
    max_megabytes = args.max_megabytes
    max_lines = args.max_lines

    
    # file_name, file_extension = os.path.splitext(input_file)
    file_size = os.path.getsize(input_file)

    total_number_of_bytes_writen = 0
    file_name_part = 1

    while total_number_of_bytes_writen < file_size:
        total_number_of_bytes_writen, file_name_part = run_pipeline(
            input_file, 
            file_name_part, 
            max_megabytes, 
            max_lines, 
            total_number_of_bytes_writen, 
            output_dir
            )

if __name__ == '__main__':
    main()
