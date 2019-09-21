from faker import Faker
fake = Faker()
from random import randint
import datetime

user = """CREATE (:USER {{\
			idUser: "{}",\
			nickname: "{}",\
			name: "{}",\
			lastName: "{}",\
			phoneNumber: {},\
			birthDate: "{}",\
			email: "{}",\
			gender: "{}",\
			emailNotifications: {},\
			picturePath: "path/to/heaven.cypher",\
			purpose: "testing"\
		}})\n\n"""

fc = """CREATE (:FC {{\
			idFc: "{}",\
			front: "{}",\
			back: "{}",\
            lastModifyDate: "{}",\
            creationDate: "{}",\
            comments: "{}"\
		}})\n\n"""

fc_group = """CREATE (:FCGroup {{\
			idFcg: "{}",\
            title: "{}",\
            lastModifyDate: "{}",\
            creationDate: "{}",\
            tags: "{}"\
		}})\n\n"""

users = ""
fcs = ""
fcgroups = ""

fcgrelationships = ""

# fcrs = ""
# # CREATE ( :USER {{ idUser: "{}" }} )-[:OWN]->(:FCGroup {{ idFcg: "{}"}})\n\n
# fcgr = """
# MATCH (u:USER), (fcg:FCGroup) WHERE u.idUser = "{}" and fcg.idFcg = "{}" CREATE (u)-[r:OWN]->(fcg) return r;\n\n
# """
#
# fcr = """
# MATCH (fc:FC), (fcg:FCGroup) WHERE fc.idFc = "{}" and fcg.idFcg = "{}" CREATE (fcg)-[r:CONTAINS]->(fc)\n\n
# """

jTotal = 5
kTotal = 26
for i in range(0, 5):
    users += user.format(str(i), fake.name(), fake.name(), fake.name(), str(randint(30000000, 99999999)),
                         datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), fake.email(), "male",
                         bool(randint(0, 1)))

    for j in range(0, 5):
        fcgroups += fc_group.format(str(jTotal), "esto es un dataset de Fcs",  datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                     datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), ["tag1", "tag2"])
        # fcgrelationships += fcgr.format(i, jTotal)
        jTotal += 1

        for k in range(0, 5):

            fcs += fc.format(kTotal, fake.text(), fake.text(), fake.date(pattern="%Y-%m-%d", end_datetime=None),
                             fake.date(pattern="%Y-%m-%d", end_datetime=None), "Esto-es-un-tag", fake.text())
            # fcrs += fcr.format(jTotal, kTotal)
            kTotal += 1

#
# + fcgrelationships +  + fcrs
total = users + fcgroups + fcs
f = open("cy.cypher", "w+")
f.write(total)
f.close()
