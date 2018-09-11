import torch

def evaluateAndShowAttention(input_sentence):
    output_words, attentions = evaluate(
        encoder1, attn_decoder1, input_sentence)
    print('input =', input_sentence)
    print('output =', ' '.join(output_words))
    # showAttention(input_sentence, output_words, attentions)

encoder1, attn_decoder1 = torch.load('./model/seq2seq_encoder_decoder.pkl')

evaluateAndShowAttention("그새끼 미친놈이네")

evaluateAndShowAttention("미친놈이 꺼져")

evaluateAndShowAttention("그새끼 재수없네")

evaluateAndShowAttention("개좋아")
