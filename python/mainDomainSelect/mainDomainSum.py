"""
对所有收集好的主域名文件进行汇总，去重，最后放入到mainDomain.txt中
使用步骤：
- 先手动收集 src给定的资产、企查查的，放入到partDomain.txt中
- 运行脚本tianyan.py、aiqicha.py、beianx.py、xiaolanben.py 四个脚本
- 最后运行该脚本
"""

#读取文件内容
def read_file(filename):
    try:
        with open(filename,'r',encoding='utf-8') as f:
            return f.readlines()    #读取文件的所有内容，按行分割成一个列表，列表中的每个元素就是文件中的一行内容（包含每行末尾的换行符 \n）
    except FileNotFoundError:
        print(f"{filename}未找到，跳过该文件")
        return []
    except Exception as e:
        print(f"读取{filename}时出错：{e}")
        return []

#主函数
def main():
    #存储去重后的主域名
    unique_domains=set()
    #输入文件列表
    input_files=['partDomain.txt','tianyan.txt','beianx.txt','xiaolanben.txt','aiqicha.txt']
    for filename in input_files:
        lines=read_file(filename)
        for line in lines:
            line=line.strip()  #去除字符串两端的空白字符,包括换行符等
            if line:
                unique_domains.add(line)

    #将结果写入mainDomain.txt中
    try:
        with open('mainDomain.txt','w',encoding='utf-8') as f:
            for domain in unique_domains:
                f.write(domain+'\n')
    except Exception as e:
        print(f"写入文件时出错：{e}")

if __name__ == '__main__':
    main()


