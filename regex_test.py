import re

regex = r"[Q)]{2}[A-Z]{4}/Q[A-Z]{4}/[IKV]{1,2}/[NBO]{1,3}/[AWEK]{1,2}/\d{3}/\d{3}/\d{4}N\d{5}W\d{3}"

test_str = ("Q) MHTG/QSPCS/IV/BO/AE/000/999/1732N08818W025")

matches = re.finditer(regex, test_str)

for matchNum, match in enumerate(matches):
    matchNum = matchNum + 1

    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum=matchNum, start=match.start(),
                                                                         end=match.end(), match=match.group()))

    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1

        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum, start=match.start(groupNum),
                                                                         end=match.end(groupNum),
                                                                         group=match.group(groupNum)))