teamName = ['dragon', 'unicorn', 'trojan', 'spartan']
for hostTeam in teamName:
    for awayTeam in teamName:
        if hostTeam != awayTeam:
            print(hostTeam+" vs "+awayTeam)
    print()
        