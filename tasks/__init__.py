from invoke import Collection
from tasks import page_load, slider_plot

namespace = Collection()

namespace.add_collection(page_load)
namespace.add_collection(slider_plot)