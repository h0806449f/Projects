import asyncio
import subprocess

semaphore = asyncio.Semaphore(5)

async def refresh_session(profile):
    async with semaphore:
        command = f"aws-vault exec {profile} -- true"
        print(f"🔄 Refreshing session for profile: {profile}")

        process = await asyncio.create_subprocess_shell(
            command,
            executable="/bin/bash",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

        stdout, stderr = await process.communicate()

        if stdout:
            out = stdout.decode().strip()
            if out:
                print(f"[{profile}] STDOUT: {out}")
        if stderr:
            err = stderr.decode().strip()
            if err:
                print(f"[{profile}] STDERR: {err}")

async def main():
    result = subprocess.run(
        ["aws-vault", "list"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    profiles = []
    for line in result.stdout.splitlines()[1:]:
        line = line.strip()
        if not line:
            continue

        profile_name = line.split()[0]

        if profile_name in ("=======", "-", "default"):
            continue

        profiles.append(profile_name)

    tasks = [refresh_session(profile) for profile in profiles]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
