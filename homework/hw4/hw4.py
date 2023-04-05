# HW4_STRFILE_DICT (ไม่ลบหรือแก้ไขบรรทัดนี้ หรือเพิ่มอะไรก่อนบรรทัดนี้ โดยเด็ดขาด)
# ดูรายละเอียดและตัวอย่างเพิ่มเติมในคำอธิบายด้านบน

def get_product_from_file(textfile):
    product = {}
    file = open(textfile, "r", encoding="UTF-8")
    for i in file:
        i = i.strip().replace(' ', '').split('=')
        if i[0] == "created_date":
            i[1] = i[1][:2] + '/' + i[1][2:4] + '/' + i[1][4:]
        product[i[0]] = i[1]
    return product

# ======================================


def cal_defect_ratio(textfile):
    product = get_product_from_file(textfile)
    scan_data = product['scan_data']
    defect_ratio = scan_data.count('+') / len(scan_data.replace(',', ''))

    return round(defect_ratio, 2)


# ======================================
def cal_defect_box_ratio(textfile):
    defect_box_ratio = 0
    product = get_product_from_file(textfile)
    scan_data = product['scan_data'].replace(',', '')
    if scan_data.count('+') == 0:
        return round(defect_box_ratio, 2)
    n = round(len(scan_data)**(1/3))
    width = []
    length = []
    height = []
    for no, i in enumerate(range(0, len(scan_data), n)):
        cube = scan_data[i:i+n]
        if '+' in cube:
            [width.append(j) for j in range(len(cube)) if cube[j] == "+"]
            length.append(no%n)
            height.append(no//n)
    w = max(width) - min(width) + 1
    l = max(length) - min(length) + 1
    h = max(height) - min(height) + 1

    defect_total = w*l*h
    cube_total = len(scan_data)
    defect_box_ratio = defect_total / cube_total

    return round(defect_box_ratio, 2)


# ======================================
def create_prod_summary_file(pids):
    if not pids:
        return
    summary = ['pid,created_date,factory_id,defect_ratio,defect_box_ratio']
    for i in sorted(pids):
        product = get_product_from_file(i + '.txt')
        data = "{},{},{},{},{}".format(i, product['created_date'], product['factory_id'], cal_defect_ratio(i + '.txt'), cal_defect_box_ratio(i + '.txt'))
        summary.append(data)

    writeFile = open('product_summary.csv', 'w')
    writeFile.write('\n'.join(summary))
    writeFile.close()
    return 


# ======================================
def create_size_summary_file(pids):
    if not pids:
        return
    sizes = [0, 0, 0]
    for i in pids:
        dbr = cal_defect_box_ratio(i + ".txt")
        if dbr < 0.33:
            sizes[0] += 1
        elif dbr >= 0.33 and dbr < 0.67:
            sizes[1] += 1
        else:
            sizes[2] += 1
    writeFile = open('size_summary.csv', 'w')
    writeFile.write('size,#\nS,{}\nM,{}\nL,{}'.format(sizes[0], sizes[1], sizes[2]))
    writeFile.close()
    return



# ======================================
# สามารถเขียนฟังก์ชันที่สร้างเองได้ในบริเวณด้านล่างนี้เท่านั้น


# print(get_product_from_file('001.txt'))
# print(cal_defect_ratio('001.txt'))
# print(cal_defect_box_ratio('001.txt'))
# create_prod_summary_file(["001","199","003","004","ABCD","002","010","009","008","007","005"])
# create_size_summary_file(["001","009","008"])