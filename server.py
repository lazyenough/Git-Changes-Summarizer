from mcp.server.fastmcp import FastMCP
import pygit2

app = FastMCP("git summarizer server")

@app.tool()
def get_git_changes(base_repo: str):
    """
    Fetches the code changes in the repository.

    Args:
    repo - Link to the repository.
    """

    repo = pygit2.Repository(base_repo)

    commit_b = repo.head.peel(pygit2.Commit)
    commit_a = commit_b.parents[0] if commit_b.parents else None # Handle initial commit

    if commit_a:
        diff = repo.diff(commit_a, commit_b)
    else:
        # Handle initial commit where there's no parent to diff against
        diff = repo.diff(None, commit_b)

    changed_lines = ""
    for patch in diff:
        for hunk in patch.hunks:
            for line in hunk.lines:
                # line.origin indicates the type of change:
                # '+' for added lines
                # '-' for deleted lines
                # ' ' for unchanged context lines
                changed_lines += f"{line.origin} {line.content.strip()}"

    
    return changed_lines


if __name__ == "__main__":
    print("Starting the server...")
    # app.run(transport="streamable-http")
    app.run(host="0.0.0.0", port="8080", transport="streamable-http")