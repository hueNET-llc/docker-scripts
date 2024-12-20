# This script is used to build Docker images using buildx and push them to Docker Hub
import os
import requests

from subprocess import PIPE, check_output, run
from time import perf_counter

try:
    WEBHOOK_URL = os.environ['BUILD_SCRIPT_DISCORD_WEBHOOKURL']
except KeyError:
    print('BUILD ERROR: No webhook URL specified')
    exit(1)

# Get the image name
# e.g. docker.io/crazymax/diun:latest
if not (IMAGE := os.environ.get('DIUN_ENTRY_IMAGE')):
    print('BUILD ERROR: No image specified')
    requests.post(
        WEBHOOK_URL,
        json={'content': f'❌ Failed to build `{IMAGE}`, missing image'}
    )
    exit(1)
print(f'Building {IMAGE}')

# Check if a provider was specified
if not (PROVIDER := os.environ.get('DIUN_ENTRY_PROVIDER')):
    print('BUILD ERROR: No provider specified')
    requests.post(
        WEBHOOK_URL,
        json={'content': f'❌ Failed to build `{IMAGE}`, missing provider'}
    )
    exit(1)

# Check if a Docker Hub username was specified
if not (DOCKER_HUB_USERNAME := os.environ.get('DOCKER_HUB_USERNAME')):
    print('BUILD ERROR: No Docker Hub username specified')
    requests.post(
        WEBHOOK_URL,
        json={'content': f'❌ Failed to build `{IMAGE}`, missing Docker Hub username'}
    )
    exit(1)

if not (PLATFORMS := os.environ.get('DIUN_ENTRY_METADATA_PLATFORMS')):
    print(f'Platforms not specified, defaulting to linux/amd64')
    PLATFORMS = 'linux/amd64'
else:
    print(f'Building for platforms {PLATFORMS}')

if PROVIDER == 'dockerfile':
    if not (OUTPUT_IMAGE := os.environ.get('DIUN_ENTRY_METADATA_OUTPUT_IMAGE')) \
    or not (OUTPUT_TAG := os.environ.get('DIUN_ENTRY_METADATA_OUTPUT_TAG')):
        print(f'BUILD ERROR: No output image or tag specified for entry image {IMAGE}')
        requests.post(
            WEBHOOK_URL,
            json={'content': f'❌ Failed to build `{IMAGE}`, missing output image or tag'}
        )
        exit(1)

    # Check if the Dockerfile doesn't exist
    if not os.path.isfile(f'/dockerfiles/{OUTPUT_IMAGE}/{OUTPUT_TAG}/Dockerfile'):
        print(f'BUILD ERROR: Dockerfile for output image {OUTPUT_IMAGE}:{OUTPUT_TAG} does not exist')
        requests.post(
            WEBHOOK_URL,
            json={'content': f'❌ Failed to build `{IMAGE}`, missing Dockerfile for `{OUTPUT_IMAGE}:{OUTPUT_TAG}`'}
        )
        exit(1)

    # Check if the Dockerfile is empty
    if os.stat(f'/dockerfiles/{OUTPUT_IMAGE}/{OUTPUT_TAG}/Dockerfile').st_size == 0:
        print(f'BUILD ERROR: Dockerfile for output image {OUTPUT_IMAGE}:{OUTPUT_TAG} is empty')
        requests.post(
            WEBHOOK_URL,
            json={'content': f'❌ Failed to build `{IMAGE}`, Dockerfile for `{OUTPUT_IMAGE}:{OUTPUT_TAG}` is empty'}
        )
        exit(1)

    # Create a builderx instance
    run(f'docker buildx create --name buildx-{OUTPUT_IMAGE}-{OUTPUT_TAG}', shell=True)

    start = perf_counter()

    # Create a buildx instance, build the image for AMD64/ARM64, and push it to the registry
    build_proc = run(
        f'docker buildx build --builder=buildx-{OUTPUT_IMAGE}-{OUTPUT_TAG} --no-cache --platform {PLATFORMS} --push -t {DOCKER_HUB_USERNAME}/{OUTPUT_IMAGE}:{OUTPUT_TAG} /dockerfiles/{OUTPUT_IMAGE}/{OUTPUT_TAG}',
        stdout=PIPE,
        stderr=PIPE,
        shell=True
    )

    time_taken = perf_counter() - start

    build_output = []
    if (stdout := build_proc.stdout.decode().strip()):
        build_output.append(f'stdout:\n{stdout}')
    if (stderr := build_proc.stderr.decode().strip()):
        build_output.append(f'stderr:\n{stderr}')

    if build_proc.returncode:
        print(f'Failed to build {IMAGE} for {PLATFORMS} after {round(time_taken, 2)}s, exited with {build_proc.returncode}')
        result = f'❌ Failed to build `{IMAGE}` for `{PLATFORMS}`\nℹ️ Build process exited with `{build_proc.returncode}`\n⏱️ Took `{round(time_taken, 2)}s`'
    else:
        print(f'Built {IMAGE} for {PLATFORMS} after {round(time_taken, 2)}s, pushed to docker.io/{DOCKER_HUB_USERNAME}/{OUTPUT_IMAGE}:{OUTPUT_TAG}')
        result = f'✅ Built `{IMAGE}` for `{PLATFORMS}`\n⬆️ Pushed to `docker.io/{DOCKER_HUB_USERNAME}/{OUTPUT_IMAGE}:{OUTPUT_TAG}`\nℹ️ Build process exited with `{build_proc.returncode}`\n⏱️ Took `{round(time_taken, 2)}s`'

    # Delete the buildx instance
    run(f'docker buildx rm buildx-{OUTPUT_IMAGE}-{OUTPUT_TAG}', shell=True)
    
    requests.post(WEBHOOK_URL, data={'content': result}, files={'file': ('output.txt', '\n\n'.join(build_output))})
