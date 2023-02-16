ARG GCP_REGISTRY_PROJECT
ARG BASE_FE_IMAGE_VERSION

# Final image based on openresty
FROM openresty/openresty:1.19.9.1-12-alpine AS nginx

RUN apk update && apk --no-cache add tini

RUN rm -rf /etc/nginx/conf.d
COPY docker/nginx/run.sh /src/run.sh

ENV PATH=/src:$PATH
RUN chown -R nobody /etc/nginx /src
RUN mkdir -m 755 /var/log/nginx

COPY --from=slam-dashboard /dep/dashboard/dist               /src/ui/dashboard/dist
COPY --from=slam-pipeline  /dep/pipeline/dist                /src/ui/dist
COPY --from=slam-dms       /dep/dms/dist                     /src/ui/dms/dist
COPY --from=slam-admin     /dep/admin/dist                   /src/ui/admin/dist
COPY --from=slam-editorv2  /dep/react-planner/dist      /src/ui/react-planner/dist
COPY --from=slam-potential_view_v2  /dep/potential-view/dist      /src/ui/potential-view/dist

WORKDIR /src/

EXPOSE 80
ENTRYPOINT ["/sbin/tini", "--"]
CMD ["/src/run.sh"]

COPY docker/nginx/nginx.conf /etc/nginx/conf.d/app.conf
