###
### Copyright (C) 2018-2019 Intel Corporation
###
### SPDX-License-Identifier: BSD-3-Clause
###

from ....lib import *
from ..util import *
from .decoder import DecoderTest

spec = load_test_spec("vc1", "decode")

class default(DecoderTest):
  def before(self):
    # default metric
    self.metric = dict(type = "ssim", miny = 0.99, minu = 0.99, minv = 0.99)
    super(default, self).before()

  @platform_tags(VC1_DECODE_PLATFORMS)
  @slash.requires(*have_gst_element("msdkvc1dec"))
  @slash.parametrize(("case"), sorted(spec.keys()))
  def test(self, case):
    vars(self).update(spec[case].copy())
    vars(self).update(
      case        = case,
      gstdecoder  = "'video/x-wmv,profile=(string)advanced'"
                    ",width={width},height={height},framerate=14/1"
                    " ! msdkvc1dec".format(**vars(self)),
    )
    self.decode()
