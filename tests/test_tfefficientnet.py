import unittest

from titans.tfefficientnet import EfficientNet


class TestEfficientNet(unittest.TestCase):
    def test_init(self):
        # scale negative
        with self.assertRaises(ValueError):
            EfficientNet(scale=-1)

        # scale too large
        with self.assertRaises(ValueError):
            EfficientNet(scale=8)

        model = EfficientNet(scale=0)
        self.assertEqual(model.scale, 0)

    def test_label_map(self):
        model = EfficientNet(scale=0)

        self.assertEqual(len(model.label_map), 1000)

        expected = ("tench", "goldfish", "great white shark")
        self.assertEqual(model.label_map[:3], expected)


if __name__ == "__main__":
    unittest.main()
    