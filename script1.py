
from bert_serving.client import BertClient
from sklearn.metrics.pairwise import cosine_similarity
#import gensim

client = BertClient()

# Load Google's pre-trained Word2Vec model.
# model =  gensim.models.KeyedVectors.load_word2vec_format('crisisNLP_word_vector.bin', binary=True)  
#model = gensim.models.KeyedVectors.load_word2vec_format('/home/nilesh/SciBert/scibert_scivocab_uncased.tar.gz', binary=True)


#text_data=[]
# filepath = 'srilanka_preprocessed.txt'
# filepath = 'distinct_imp_senetences.txt'
filepath = 'test1.txt'

f5=open('output4.txt','w')

def maxn(list1, N): 
    final_list = [] 
  
    for i in range(0, N):  
        max1 = (0,0)
          
        for j in range(len(list1)):      
            if list1[j][0] > max1[0]: 
                max1 = list1[j]; 
                  
        list1.remove(max1); 
        final_list.append(max1) 
          
    return final_list 		

with open(filepath) as fp:
	for cnt, line in enumerate(fp):
		f5.write(str(cnt))
		result = list()
		with open(filepath) as fp1: 
			for cnt1, line1 in enumerate(fp1):
				#start  =  time()	
				list1 = list()
				list2 = list()
				
				list1.append(line.lower())
				list2.append(line1.lower())	
				print(list1)
				print(list2)
				# sentence_obama = line.lower().split()
				# sentence_president = line1.lower().split()
				# sentence_obama = [w for w in sentence_obama]
				# sentence_president = [w for w in sentence_president]
				v1 = client.encode(list1)
				v2 = client.encode(list2)
				distance = cosine_similarity(v1, v2)

				#model.init_sims(replace=True)  # Normalizes the vectors in the word2vec class.
				#distance = model.wmdistance(sentence_obama, sentence_president)
				# f5.write('\t'+ str(distance))
				tu = (distance,cnt1)
				result.append(tu)

				print("Line {}: {}".format(cnt, line))
				print("Line {}: {}".format(cnt1, line1))
				#print("distance b/w sentence cnt and cnt1  = %.3f" % distance )
				#print('Cell took %.2f seconds to run.' % (time() - start))      
				print("-----------------------------------------") 		
			
		result = maxn(result,5)
		f5.write('\t'+ str(result))
		f5.write('\n')
f5.close()



