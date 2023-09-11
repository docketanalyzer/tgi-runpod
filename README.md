# tgi-runpod

Simple RunPod wrapper for [Text Generation Inference](https://github.com/huggingface/text-generation-inference)

#### Serverless Container

1. Use `nadahlberg/tgi-runpod:serverless`
2. Attach network volume with downloaded model (see Pod Container below)
3. Configure env including any TGI arguments 

```
HUGGINGFACE_HUB_CACHE=/runpod-volume/models/
HUGGING_FACE_HUB_TOKEN=<Your token here>
MODEL_ID=TheBloke/Llama-2-70B-chat-GPTQ
QUANTIZE=gptq

# Other TGI arguments e.g.
MAX_INPUT_LENGTH=2048
MAX_BATCH_PREFILL_TOKENS=4096
MAX_TOTAL_TOKENS=4096

# If (and only if!) using multiple GPUs
CUDA_VISIBLE_DEVICES=0,1
```

#### Pod Container

To run TGI in a pod:

1. Use `nadahlberg/tgi-runpod:pod`
2. Download model with `text-generation-launcher --model-id TheBloke/Llama-2-70B-chat-GPTQ --quantize gptq`
3. Remember to set your cache location in env

```
HUGGINGFACE_HUB_CACHE=/workspace/models/
```

#### Usage

Inputs should include `prompt` and `args`.  Prompt can be a list of prompts (recommended to max out utilization) and args gets passed to the TGI call (see their [API Docs](https://huggingface.github.io/text-generation-inference/))

```
{
    'input': {
        'prompt': ['Hello', 'Wow'],
        'args': {'max_new_tokens': 100}
    }
}
```




