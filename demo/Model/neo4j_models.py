# -*- coding: utf-8 -*-
from py2neo import Graph,Node,Relationship,NodeMatcher
#版本说明：Py2neo v4
class Neo4j_Handle():
	graph = None
	matcher = None
	def __init__(self):
		print("Neo4j Init ...")

	def connectDB(self):
		# self.graph = Graph("bolt://localhost:7687", username="neo4j", password="LH980512")
		self.graph = Graph("bolt://localhost:7687/", auth=("neo4j", "LH980512"))
		self.matcher = NodeMatcher(self.graph)

	#实体查询，用于命名实体识别
	# def matchEntityItem(self,value):
	# 	answer = self.graph.run("MATCH (entity1) WHERE entity1.name = \"" + value + "\" RETURN entity1").data()
	# 	# answer = self.graph.run("MATCH (entity1) WHERE entity1.bingli_id = \"" + value + "\" RETURN entity1").data()
	# 	return answer

	#实体查询
	def getEntityRelationbyEntity(self,value):
		#查询实体：不考虑实体类型，只考虑关系方向
		answer = self.graph.run("MATCH (entity1) - [rel] -> (entity2)  WHERE entity1.name = \"" + value + "\" RETURN rel,entity2").data()
		# answer = self.graph.run("MATCH (entity1) - [rel] -> (entity2)  WHERE entity1.bingli_id = \"" + value + "\" RETURN rel,entity2").data()
		if(len(answer) == 0):
			#查询实体：不考虑关系方向
			answer = self.graph.run("MATCH (entity1) - [rel] - (entity2)  WHERE entity1.name = \"" + value + "\" RETURN rel,entity2").data()
			# answer = self.graph.run("MATCH (entity1) - [rel] - (entity2)  WHERE entity1.bingli_id = \"" + value + " \" RETURN rel,entity2").data()
		print(answer)
		return answer

	#关系查询:实体1
	def findRelationByEntity1(self,entity1):

		# answer = self.graph.run("MATCH (n1:Bank {name:\""+entity1+"\"})- [rel] -> (n2) RETURN n1,rel,n2" ).data()
		# answer = self.graph.run("MATCH (n1:disease {name:\"" + entity1 + " \"})- [rel] -> (n2) RETURN n1,rel,n2").data()
		answer = self.graph.run("MATCH (n1:病例 {name:\""+entity1+"\"})- [rel] -> (n2) RETURN n1,rel,n2").data()

		if(len(answer) == 0):
			# answer = self.graph.run("MATCH (n1:Serise {name:\""+entity1+" \"})- [rel] - (n2) RETURN n1,rel,n2" ).data()
			# answer = self.graph.run("MATCH (n1:Food {name:\""+entity1+" \"})- [rel] - (n2) RETURN n1,rel,n2" ).data()
			answer = self.graph.run("MATCH (n1:外出地址 {name:\""+entity1+"\"})- [rel] - (n2) RETURN n1,rel,n2").data()

		return answer

	#关系查询：实体2
	def findRelationByEntity2(self,entity1):

		# answer = self.graph.run("MATCH (n1)<- [rel] - (n2:Bank {name:\""+entity1+"\"}) RETURN n1,rel,n2" ).data()
		answer = self.graph.run("MATCH (n1)<- [rel] - (n2:病例 {name:\""+entity1+"\"}) RETURN n1,rel,n2" ).data()
		if(len(answer) == 0):

			# answer = self.graph.run("MATCH (n1) - [rel] - (n2:Serise {name:\""+entity1+" \"}) RETURN n1,rel,n2" ).data()
			answer = self.graph.run("MATCH (n1) - [rel] - (n2:外出地址 {name:\""+entity1+"\"}) RETURN n1,rel,n2" ).data()
		return answer

	#关系查询：实体1+关系
	def findOtherEntities(self,entity,relation):
		# answer = self.graph.run("MATCH (n1:Bank {name:\"" + entity + "\"})- [rel:Subtype {type:\""+relation+"\"}] -> (n2) RETURN n1,rel,n2" ).data()
		answer = self.graph.run("MATCH (n1:病例 {name:\""+entity+"\"})- [rel:上课 {type:\""+relation+"\"}] -> (n2) RETURN n1,rel,n2" ).data()
		if(len(answer) == 0):
			answer = self.graph.run("MATCH (n1:病例 {name:\""+entity+"\"})- [rel:上班 {type:\""+relation+"\"}] -> (n2) RETURN n1,rel,n2" ).data()
		if (len(answer) == 0):
			answer = self.graph.run("MATCH (n1:病例 {name:\"" + entity + "\"})- [rel:家属 {type:\"" + relation + "\"}] -> (n2) RETURN n1,rel,n2").data()
		if (len(answer) == 0):
				answer = self.graph.run("MATCH (n1:病例 {name:\"" + entity + "\"})- [rel:办业务 {type:\"" + relation + "\"}] -> (n2) RETURN n1,rel,n2").data()
		if (len(answer) == 0):
			answer = self.graph.run("MATCH (n1:病例 {name:\"" + entity + "\"})- [rel:参加宴会 {type:\"" + relation + "\"}] -> (n2) RETURN n1,rel,n2").data()
		if (len(answer) == 0):
			answer = self.graph.run("MATCH (n1:病例 {name:\"" + entity + "\"})- [rel:同事 {type:\"" + relation + "\"}] -> (n2) RETURN n1,rel,n2").data()
		if (len(answer) == 0):
			answer = self.graph.run("MATCH (n1:病例 {name:\"" + entity + "\"})- [rel:取快递 {type:\"" + relation + "\"}] -> (n2) RETURN n1,rel,n2").data()
		if (len(answer) == 0):
			answer = self.graph.run("MATCH (n1:病例 {name:\"" + entity + "\"})- [rel:同住家属 {type:\"" + relation + "\"}] -> (n2) RETURN n1,rel,n2").data()
		if (len(answer) == 0):
			answer = self.graph.run("MATCH (n1:病例 {name:\"" + entity + "\"})- [rel:同楼栋邻居 {type:\"" + relation + "\"}] -> (n2) RETURN n1,rel,n2").data()
		if (len(answer) == 0):
			answer = self.graph.run("MATCH (n1:病例 {name:\"" + entity + "\"})- [rel:密切接触者 {type:\"" + relation + "\"}] -> (n2) RETURN n1,rel,n2").data()
		if (len(answer) == 0):
			answer = self.graph.run("MATCH (n1:病例 {name:\"" + entity + "\"})- [rel:就餐 {type:\"" + relation + "\"}] -> (n2) RETURN n1,rel,n2").data()
		if (len(answer) == 0):
			answer = self.graph.run("MATCH (n1:病例 {name:\"" + entity + "\"})- [rel:打牌 {type:\"" + relation + "\"}] -> (n2) RETURN n1,rel,n2").data()
		if (len(answer) == 0):
			answer = self.graph.run("MATCH (n1:病例 {name:\"" + entity + "\"})- [rel:接种疫苗 {type:\"" + relation + "\"}] -> (n2) RETURN n1,rel,n2").data()
		if (len(answer) == 0):
			answer = self.graph.run("MATCH (n1:病例 {name:\"" + entity + "\"})- [rel:购物 {type:\"" + relation + "\"}] -> (n2) RETURN n1,rel,n2").data()
		if (len(answer) == 0):
			answer = self.graph.run("MATCH (n1:病例 {name:\"" + entity + "\"})- [rel:进行核酸检测 {type:\"" + relation + "\"}] -> (n2) RETURN n1,rel,n2").data()
		if (len(answer) == 0):
			answer = self.graph.run("MATCH (n1:病例 {name:\"" + entity + "\"})- [rel:活动 {type:\"" + relation + "\"}] -> (n2) RETURN n1,rel,n2").data()


		return answer

	#关系查询：关系+实体2
	def findOtherEntities2(self,entity,relation):
		print("findOtherEntities2==")
		print(entity,relation)
		# answer = self.graph.run("MATCH (n1)- [rel:RELATION {type:\""+relation+"\"}] -> (n2:Bank {name:\"" + entity + "\"}) RETURN n1,rel,n2" ).data()
		answer = self.graph.run("MATCH (n1)- [rel:上课 {type:\""+relation+"\"}] -> (n2:外出地址 {name:\"" + entity + "\"}) RETURN n1,rel,n2" ).data()
		if(len(answer) == 0):
			answer = self.graph.run("MATCH (n1)- [rel:上班 {type:\""+relation+"\"}] -> (n2:外出地址 {name:\"" + entity + "\"}) RETURN n1,rel,n2" ).data()
			if(len(answer) == 0):
				answer = self.graph.run("MATCH (n1)- [rel:家属 {type:\""+relation+"\"}] -> (n2:病例 {name:\"" + entity + "\"}) RETURN n1,rel,n2" ).data()
			if(len(answer) == 0):
				answer = self.graph.run("MATCH (n1)- [rel:办业务 {type:\""+relation+"\"}] -> (n2:外出地址 {name:\"" + entity + "\"}) RETURN n1,rel,n2" ).data()
			if(len(answer) == 0):
				answer = self.graph.run("MATCH (n1)- [rel:参加宴会 {type:\""+relation+"\"}] -> (n2:外出地址 {name:\"" + entity + "\"}) RETURN n1,rel,n2" ).data()
			if(len(answer) == 0):
				answer = self.graph.run("MATCH (n1)- [rel:同事 {type:\""+relation+"\"}] -> (n2:病例 {name:\"" + entity + "\"}) RETURN n1,rel,n2" ).data()
			if(len(answer) == 0):
				answer = self.graph.run("MATCH (n1)- [rel:取快递 {type:\"" + relation + "\"}] -> (n2:外出地址 {name:\"" + entity + "\"}) RETURN n1,rel,n2").data()
			if (len(answer) == 0):
				answer = self.graph.run("MATCH (n1)- [rel:同住家属 {type:\"" + relation + "\"}] -> (n2:病例 {name:\"" + entity + "\"}) RETURN n1,rel,n2").data()
			if (len(answer) == 0):
				answer = self.graph.run("MATCH (n1)- [rel:同楼栋邻居 {type:\"" + relation + "\"}] -> (n2:病例 {name:\"" + entity + "\"}) RETURN n1,rel,n2").data()
			if (len(answer) == 0):
				answer = self.graph.run("MATCH (n1)- [rel:密切接触者 {type:\"" + relation + "\"}] -> (n2:病例 {name:\"" + entity + "\"}) RETURN n1,rel,n2").data()
			if (len(answer) == 0):
				answer = self.graph.run("MATCH (n1)- [rel:就餐 {type:\"" + relation + "\"}] -> (n2:外出地址 {name:\"" + entity + "\"}) RETURN n1,rel,n2").data()
			if (len(answer) == 0):
				answer = self.graph.run("MATCH (n1)- [rel:打牌 {type:\"" + relation + "\"}] -> (n2:外出地址 {name:\"" + entity + "\"}) RETURN n1,rel,n2").data()
			if (len(answer) == 0):
				answer = self.graph.run("MATCH (n1)- [rel:接种疫苗 {type:\"" + relation + "\"}] -> (n2:外出地址 {name:\"" + entity + "\"}) RETURN n1,rel,n2").data()
			if (len(answer) == 0):
				answer = self.graph.run("MATCH (n1)- [rel:购物 {type:\"" + relation + "\"}] -> (n2:外出地址 {name:\"" + entity + "\"}) RETURN n1,rel,n2").data()
			if (len(answer) == 0):
				answer = self.graph.run("MATCH (n1)- [rel:进行核酸检测 {type:\"" + relation + "\"}] -> (n2:外出地址 {name:\"" + entity + "\"}) RETURN n1,rel,n2").data()
			if (len(answer) == 0):
				answer = self.graph.run("MATCH (n1)- [rel:活动 {type:\"" + relation + "\"}] -> (n2:外出地址 {name:\"" + entity + "\"}) RETURN n1,rel,n2").data()
		return answer

	#关系查询：实体1+实体2
	def findRelationByEntities(self,entity1,entity2):
		answer = self.graph.run("MATCH (n1:病例 {name:\"" + entity1 + "\"})- [rel] - (n2:病例{name:\""+entity2+"\"}) RETURN n1,rel,n2" ).data()
		if(len(answer) == 0):
			answer = self.graph.run("MATCH (n1:病例 {name:\"" + entity1 + "\"})- [rel] -> (n2:外出地址{name:\""+entity2+"\"}) RETURN n1,rel,n2" ).data()
		if(len(answer) == 0):
			answer = self.graph.run("MATCH (n1:外出地址 {name:\"" + entity1 + "\"})- [rel] - (n2:病例{name:\""+entity2+"\"}) RETURN n1,rel,n2" ).data()
		# if(len(answer) == 0):
		# 	answer = self.graph.run("MATCH (n1:Serise {name:\"" + entity1 + "\"})- [rel] -> (n2:Serise{name:\""+entity2+" \"}) RETURN n1,rel,n2" ).data()
		return answer

	#查询数据库中是否有对应的实体-关系匹配
	def findEntityRelation(self,entity1,relation,entity2):
		# answer = self.graph.run("MATCH (n1:Bank {name:\"" + entity1 + "\"})- [rel:subbank {type:\""+relation+"\"}] -> (n2:Bank{name:\""+entity2+"\"}) RETURN n1,rel,n2" ).data()
		answer = self.graph.run("MATCH (n1:病例 {name:\"" + entity1 + "\"})- [rel:上课 {type:\""+relation+"\"}] - (n2:外出地址{name:\""+entity2+"\"}) RETURN n1,rel,n2" ).data()
		# if(len(answer) == 0):
			# answer = self.graph.run("MATCH (n1:Bank {name:\"" + entity1 + "\"})- [rel:subbank {type:\""+relation+"\"}] -> (n2:Serise{name:\""+entity2+"\"}) RETURN n1,rel,n2" ).data()
		if(len(answer) == 0):
			answer = self.graph.run("MATCH (n1:病例 {name:\"" + entity1 + "\"})- [rel:上班 {type:\""+relation+"\"}] - (n2:外出地址{name:\""+entity2+"\"}) RETURN n1,rel,n2" ).data()
		if(len(answer) == 0):
			answer = self.graph.run("MATCH (n1:病例 {name:\"" + entity1 + "\"})- [rel:办业务 {type:\""+relation+"\"}] - (n2:外出地址{name:\""+entity2+"\"}) RETURN n1,rel,n2" ).data()
		if(len(answer) == 0):
			answer = self.graph.run("MATCH (n1:病例 {name:\"" + entity1 + "\"})- [rel:参加宴会 {type:\""+relation+"\"}] - (n2:外出地址{name:\""+entity2+"\"}) RETURN n1,rel,n2" ).data()
		if(len(answer) == 0):
			answer = self.graph.run("MATCH (n1:病例 {name:\"" + entity1 + "\"})- [rel:同事 {type:\""+relation+"\"}] - (n2:病例{name:\""+entity2+"\"}) RETURN n1,rel,n2" ).data()
		if(len(answer) == 0):
			answer = self.graph.run("MATCH (n1:病例 {name:\"" + entity1 + "\"})- [rel:取快递 {type:\""+relation+"\"}] - (n2:外出地址{name:\""+entity2+"\"}) RETURN n1,rel,n2" ).data()
		if(len(answer) == 0):
			answer = self.graph.run("MATCH (n1:病例 {name:\"" + entity1 + "\"})- [rel:同住家属 {type:\""+relation+"\"}] - (n2:病例{name:\""+entity2+"\"}) RETURN n1,rel,n2" ).data()
		if(len(answer) == 0):
			answer = self.graph.run("MATCH (n1:病例 {name:\"" + entity1 + "\"})- [rel:同楼栋邻居 {type:\""+relation+"\"}] - (n2:病例{name:\""+entity2+"\"}) RETURN n1,rel,n2" ).data()
		if(len(answer) == 0):
			answer = self.graph.run("MATCH (n1:病例 {name:\"" + entity1 + "\"})- [rel:密切接触者 {type:\""+relation+"\"}] - (n2:病例{name:\""+entity2+"\"}) RETURN n1,rel,n2" ).data()
		if(len(answer) == 0):
			answer = self.graph.run("MATCH (n1:病例 {name:\"" + entity1 + "\"})- [rel:就餐 {type:\""+relation+"\"}] - (n2:外出地址{name:\""+entity2+"\"}) RETURN n1,rel,n2" ).data()
		if(len(answer) == 0):
			answer = self.graph.run("MATCH (n1:病例 {name:\"" + entity1 + "\"})- [rel:打牌 {type:\""+relation+"\"}] - (n2:外出地址{name:\""+entity2+"\"}) RETURN n1,rel,n2" ).data()
		if(len(answer) == 0):
			answer = self.graph.run("MATCH (n1:病例 {name:\"" + entity1 + "\"})- [rel:接种疫苗 {type:\""+relation+"\"}] - (n2:外出地址{name:\""+entity2+"\"}) RETURN n1,rel,n2" ).data()
		if(len(answer) == 0):
			answer = self.graph.run("MATCH (n1:病例 {name:\"" + entity1 + "\"})- [rel:购物 {type:\""+relation+"\"}] - (n2:外出地址{name:\""+entity2+"\"}) RETURN n1,rel,n2" ).data()
		if(len(answer) == 0):
			answer = self.graph.run("MATCH (n1:病例 {name:\"" + entity1 + "\"})- [rel:进行核酸检测 {type:\""+relation+"\"}] - (n2:外出地址{name:\""+entity2+"\"}) RETURN n1,rel,n2" ).data()
		if(len(answer) == 0):
			answer = self.graph.run("MATCH (n1:病例 {name:\"" + entity1 + "\"})- [rel:活动 {type:\""+relation+"\"}] - (n2:外出地址{name:\""+entity2+"\"}) RETURN n1,rel,n2" ).data()

		return answer
