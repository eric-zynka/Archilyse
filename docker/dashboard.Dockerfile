ARG GCP_REGISTRY_PROJECT
ARG BASE_FE_IMAGE_VERSION

# Compiles dashboard code
FROM slam_base_fe:$BASE_FE_IMAGE_VERSION as dashboard
WORKDIR /dep/dashboard
COPY /docker/.env /dep/dashboard/.env
COPY /docker/.env.local /dep/dashboard/.env.local
COPY /ui/dashboard /dep/dashboard
ENV NODE_OPTIONS=--max-old-space-size=6144
RUN npm run build
