# Poker Card Mind reading
## Card encoding scheme
- From the card deck randomly chooses 5 cards, with the 4 cards within these 5 cards, encode the last hidden card.

## Algorithm
1. Encode the suite of the hidden using the first card. This works due to piegonhole principle
2. Think of a encoding scheme using the last 3 cards, encoding scheme here is the ordering in values magnitude of the numbers. First determine the ordering of the Suites. Here CDHS is used.
3. CLUB,DIAMOND,HEART,SPADES.(CDHS) meaning from largest to smallest rank. Thus the ordering of last 3 cards can be used to indicate the offset.
4. Think modular arithmetic, that is think about the number 1~13 not in a linear way, if we think in a linear way, 1~13, the maximum distance we can cover using 3 cards left is only 1~6. But is a circular manner.
5. Choose the suitable card for encoding.