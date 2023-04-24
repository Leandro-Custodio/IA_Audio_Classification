## Install the TensorFlow Lite runtime

```
sh setup.sh
```

## Run the example

```
python3 classify.py
```

*   You can optionally specify the `model` parameter to set the TensorFlow Lite
    model to be used:
    *   The default value is `yamnet.tflite`
*   You can optionally specify the `maxResults` parameter to limit the list of
    classification results:
    *   Supported value: A positive integer.
    *   Default value: `5`.
*   Example usage:

```
python3 classify.py \
  --model yamnet.tflite \
  --maxResults 5
```
