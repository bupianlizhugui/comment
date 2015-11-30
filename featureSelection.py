# coding:gbk
__author__ = 'weiguangshun'
import math
import codecs


# ���㿨�����ٳ���һ�����������յ�������û��Ӱ��
def Chi(a, b, c, d):
    return pow((a*b-b*c), 2)/float((a+c)*(a+b)*(b+d)*(c+d))


# �õ�ÿ������Ĵʵ䣨��ȥ�ظ��Ĵ��,��ÿ�������List����ȥ���ظ��Ĵ��Ϊ�˼���ÿ�������д�����ֵ�tf��
def getClassDic(filename):
    fr = codecs.open(filename,'r','gbk')
    str_lines = fr.readlines()
    word_set = set()
    word_list = []
    for line in str_lines:
        words = line.strip().split(' ')
        word_list.append(words)
        word_set = word_set | set(words)
    return word_set, word_list


#����Chiֵѡ������,���յ�����ҪΪ�������������Ĳ�
def selectFeature(word_set, word_list, K):
    feature = set()
    length = len(word_set)
    for i in range(length): # ��������ֱ����
        topK = []
        class_item_chi = {}
        for word in word_set[i]:
            a = 0; b = 0; c = 0; d = 0;
            for j in range(len(word_list)): # ��������ֱ����
                for w_list in word_list[j]:
                    if j == i:
                        if word in w_list:
                            a += 1
                        else:
                            c += 1
                    else:
                        if word in w_list:
                            b += 1
                        else:
                            d += 1
            chi = Chi(a, b, c, d)
            class_item_chi[word] = chi
        sorted_item_chi = sorted(class_item_chi.items(), key=lambda d:d[1], reverse=True)
        for k in range(K):
            topK.append(sorted_item_chi[k][0])
        feature = feature | set(topK) # �����������feature���кϲ�
    return list(feature)  # feature is a list

def tf_cal(feature, word_list_i):
    tf = {}
    for word in feature:
        tf.setdefault(word, 0)
        if word in word_list_i:
            cnt = word_list_i.count(word)
            tf[word] = cnt

def df_wirte_to_file(filename, feature, sample, classLabel):
    fw = codecs.open(filename, 'w', 'gbk')
    for word in feature:
        count = 0
        for s in sample:
            if word in s:
                count += 1
        fw.write(classLabel)
        fw.write('\t')
        fw.write(feature.index(word))
        fw.write(':')
        fw.write(count)
    fw.write('\n')


# def weight_cal(feature, sample):
#     for word in feature:

# ����ÿ��feature��df
# def dffeature(feature, sample):
#     df = {}
#     for word in feature:
#         df.setdefault(word, 0)
#         for word_list in sample:
#             if word in word_list:
#                 df[word] += 1
#     return df
#
#
# # ����ÿ�������������ʵ�Ȩ�أ�Ȩ�ؼ��㷽��Ϊ tf*idf
# def calc_weight(feature, word_list, df):
#     for w_list in word_list:
#         d = {}
#         for word in feature:
#             d.setdefault(word, 0)
#             tf = w_list.count(word)/float(len(word_list))
#             idf = math.log()




