ARG GCP_REGISTRY_PROJECT
ARG BASE_FE_IMAGE_VERSION

# Compiles Potential View V2 code
FROM slam_base_fe:$BASE_FE_IMAGE_VERSION as potential_view_v2
WORKDIR /dep/potential-view
COPY /docker/.env /dep/potential-view/.env
COPY /docker/.env.local /dep/potential-view/.env.local
COPY /ui/potential-view /dep/potential-view
ENV NODE_OPTIONS=--max-old-space-size=6144
RUN npm run build