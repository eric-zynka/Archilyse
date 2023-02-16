ARG GCP_REGISTRY_PROJECT
ARG BASE_FE_IMAGE_VERSION

# Compiles admin code
FROM slam_base_fe:$BASE_FE_IMAGE_VERSION as admin
WORKDIR /dep/admin/
COPY /docker/.env /dep/admin/.env
COPY /docker/.env.local /dep/admin/.env.local
COPY /ui/admin/ /dep/admin/
ENV NODE_OPTIONS=--max-old-space-size=6144
RUN npm run build
