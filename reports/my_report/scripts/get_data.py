import os

def main():
    pass

if __name__ == "__main__":
    # https://quarto.org/docs/projects/scripts.html#pre-and-post-render
    if os.getenv("QUARTO_PROJECT_RENDER_ALL"):
        main()
    else:
        print("Skipped running {__name__}.py because it was not a full project render")
