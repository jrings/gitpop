import github3

import pandas as pd

def access_github(org, repo, user, password):
    g = github3.login(user, password)

    r = g.repository(org, repo)

    titles, labels, bodies, closed = [], [], [], []
    for issue in r.iter_issues(state="all"):
        titles.append(issue.title)
        bodies.append(issue.body)
        labels.append([x.name for x in issue.labels])
        closed.append(issue.closed_at)

        X = pd.DataFrame({"title": titles, "body": bodies, "labels": labels, "closed_at": closed})
        X.to_csv("/tmp/issues.csv", index=False)

