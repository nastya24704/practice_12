def justify_text(text, width):
    words = text.split()
    lines = []
    current_line = []
    current_length = 0
    
    for word in words:
        if current_length + len(word) + len(current_line) > width:
            lines.append(current_line)
            current_line = []
            current_length = 0
        current_line.append(word)
        current_length += len(word)
    
    if current_line:
        lines.append(current_line)
    
    justified_lines = []
    for i in range(len(lines)):
        line = lines[i]
        if i == len(lines) - 1 or len(line) == 1:
            justified_lines.append(' '.join(line))
        else:
            total_spaces = width - sum(len(word) for word in line)
            gaps = len(line) - 1
            base_spaces = total_spaces // gaps
            extra_spaces = total_spaces % gaps
          
            justified_line = []
            for j in range(gaps):
                justified_line.append(line[j])
                spaces = base_spaces + (1 if j < extra_spaces else 0)
                justified_line.append(' ' * spaces)
            
            justified_line.append(line[-1])
            justified_lines.append(''.join(justified_line))
    
    return justified_lines

text = "Дан текст. По указанному количеству символов в одной строке колонки, получите такую колонку текста с выравниванием по ширине, перенося слова в следующую строку и расставляя равномерно нужное количество пробелов между словами."
width = 30

justified = justify_text(text, width)
for line in justified:
    print(line)
