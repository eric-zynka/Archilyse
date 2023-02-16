ARG GCP_REGISTRY_PROJECT
ARG BASE_FE_IMAGE_VERSION

# Compiles dms code
FROM slam_base_fe:$BASE_FE_IMAGE_VERSION as dms
WORKDIR /dep/dms/
COPY /docker/.env /dep/dms/.env
COPY /docker/.env.local /dep/dms/.env.local
COPY /ui/dms/ /dep/dms/
ENV NODE_OPTIONS=--max-old-space-size=6144
RUN npm run build
