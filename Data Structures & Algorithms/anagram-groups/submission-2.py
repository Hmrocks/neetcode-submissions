class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
                # Map each letter-count pattern to the words with that pattern.
        groups = {}

        # Process each word in the input list.
        for word in strs:
            # Make 26 counters, one for each lowercase letter a through z.
            counts = [0] * 26

            # Count the letters in this word.
            for char in word:
                # Convert the letter to an index: a -> 0, b -> 1, ..., z -> 25.
                index = ord(char) - ord("a")

                # Record one more occurrence of this letter.
                counts[index] += 1

            # Tuples can be dictionary keys; lists cannot.
            # Words that are anagrams have identical count tuples.
            key = tuple(counts)
            

            # Create a new group the first time we see this letter pattern.
            if key not in groups:
                groups[key] = []

            # Add the current word to its anagram group.
            groups[key].append(word)

        # Return the dictionary's grouped word lists.
        return list(groups.values())