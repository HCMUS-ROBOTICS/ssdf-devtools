import torchvision
from torch.utils.tensorboard import SummaryWriter
from PIL import Image


class TensorboardLogger:
    def __init__(self, path):
        assert path != None, "path is None"
        self.writer = SummaryWriter(log_dir=path)

    def update_scalar(self, tag, value, step):
        self.writer.add_scalar(tag, value, step)

    def update_loss(self, phase, value, step):
        self.update_scalar(f"{phase}/loss", value, step)

    def update_metric(self, phase, metric, value, step):
        self.update_scalar(f"{phase}/{metric}", value, step)

    def update_lr(self, gid, value, step):
        self.update_scalar(f"lr/group_{gid}", value, step)

    def update_figure(self, tag, image, step):
        self.writer.add_figure(tag, image, step)


def image_batch_show(batch, ncol=5, fig_size=(30, 10), normalize=False):
    grid_img = torchvision.utils.make_grid(batch, nrow=ncol, normalize=normalize)
    return grid_img.float().cpu()


def image_batch_show_with_title(batch, title=[], ncol=5, fig_size=(30, 10), show=False):
    NotImplemented