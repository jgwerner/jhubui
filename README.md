# Custom JupyterHub UI for K8s

Basic UI customization for the JupyterHub.

## Configuration

[These configuration instructions](https://discourse.jupyter.org/t/customizing-jupyterhub-on-kubernetes/1769/3) provide a nice alternative to baking the custom templates within the image.

Append the config below to your standard config to use the custom templates provided with this repo:

```python
jupyterhub:
  hub:
    # clone custom JupyterHub templates into a volume
    initContainers:
      - name: git-clone-templates
        image: alpine/git
        args:
          - clone
          - --single-branch
          - --branch=master
          - --depth=1
          - --
          - https://github.com/illumidesk/k8s-jhub-ui.git
          - /etc/jupyterhub/custom
        securityContext:
          runAsUser: 0
        volumeMounts:
          - name: custom-templates
            mountPath: /etc/jupyterhub/custom
    extraVolumes:
      - name: custom-templates
        emptyDir: {}
    extraVolumeMounts:
      - name: custom-templates
        mountPath: /etc/jupyterhub/custom

    extraConfig:
      templates: |
        c.JupyterHub.template_paths = ['/etc/jupyterhub/custom/jupyterhub/templates']
```

Lemon squeezy ;-)

## License

MIT
