from fastapi import APIRouter, HTTPException, Query
import requests

router = APIRouter()
GITHUB_API_URL = "https://api.github.com"

@router.get("/{user}")
def list_gists(
    user: str,
    page: int = Query(1, ge=1),
    per_page: int = Query(10, ge=1, le=100)
):
    
    """Fetch public gists for a GitHub user, with pagination."""

    url = f"{GITHUB_API_URL}/users/{user}/gists"
    resp = requests.get(url, params={"page": page, "per_page": per_page})

    if resp.status_code != 200:
        raise HTTPException(status_code=resp.status_code,
                            detail=f"Failed to fetch gists for {user}")

    gists = resp.json()
    gist_list = []
    for gist in gists:
        gist_list.append({
            "id": gist.get("id"),
            "description": gist.get("description"),
            "url": gist.get("html_url"),
            "files": list(gist.get("files", {}).keys())
        })

    return {"user": user, "page": page, "per_page": per_page, "gists": gist_list}
