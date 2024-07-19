import uvicorn


def main():
    uvicorn.run("web.app:app", port=8020, reload=True, log_level="info")
    return 0


if __name__ == '__main__':
    exit(main())
