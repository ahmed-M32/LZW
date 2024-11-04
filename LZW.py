with open('data.txt', 'r') as file:
    data = file.read()  

def lzw_compress(txt):
    dict_size = 256
    dict = {}
    compressed_txt = []
    
    for i in range(0, 256):
        dict[chr(i)] = i
    
    current = ""
    
    for i in range(0, len(txt)):
        combined = current + txt[i]
        
        if combined in dict.keys():
            current = combined
        else: 
            if dict.get(current):
                compressed_txt.append(dict[current])
            
            dict[combined] = dict_size  
            dict_size += 1
            current = txt[i]
    
    if current:
        compressed_txt.append(dict.get(current))   
    
    with open("compressed.txt", "w") as file:
        file.write(",".join(map(str, compressed_txt)))  

def lzw_decompress():
    with open('compressed.txt', 'r') as file:
        compressed_data = file.read()  

    compressed_data = list(map(int, compressed_data.split(",")))
    
    dict_size = 255
    dict2 = {i: chr(i) for i in range(dict_size)}
    
    decompressed_data = ""
    current = dict2[compressed_data[0]]
    
    for i in range(1, len(compressed_data)):
        next_letter = compressed_data[i]
        
        if next_letter in dict2.keys():
            dict2[dict_size + 1] = current + dict2[next_letter][0]
        else:
            dict2[dict_size] = current + current[0]
        
        dict_size += 1
        
        decompressed_data += current
        current = dict2[next_letter]
        
    decompressed_data += current
    
    with open("decompressed.txt", "w") as file:
        file.write(decompressed_data)
    
    return decompressed_data

lzw_compress(data)

if data == lzw_decompress():
    print("job done")
