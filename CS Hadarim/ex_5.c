#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>

#define TRUE 1
#define FALSE 0

/*****************************
* Struct called Word which is a Node in a linked list of words
* has variable next which is the next Word in linked list
* and char** translations (array of strings) which holds 
* the translations in different languages if the word 
*******************************/
typedef struct Word{
    char** translations;
    struct Word* next;
} Word;

/*****************************
 * Struct called Dictionary which has char** languages where each char* 
 * represents a language in the dictionary. 
 * Has int numOfLanguages is the number of languages int the dictionary 
 * Has variable Word* pointer to first Node in linked list of words.  
*******************************/
typedef struct {
    char** languages;
    int numOfLanguages;
    Word* wordList;
} Dictionary;

/*****************************
* Function Name: flush 
* Input: None 
* Output: None 
* Function Operation: flushes buffer until enter 
*******************************/
void flush(){
    int ch;
    while ((ch = getchar()) != '\n');
}

/*****************************
* Function Name: menu 
* Input: None 
* Output: None 
* Function Operation: prints menu and returns option user wrote (int) 
*******************************/
int menu(){

    printf("Welcome to the dictionaries manager!\n"
           "Choose an option:\n"
           "1. Create a new dictionary.\n"
           "2. Add a word to a dictionary.\n"
           "3. Delete a word from a dictionary.\n"
           "4. Find a word in a dictionary.\n"
           "5. Delete a dictionary.\n"
           "6. Exit.\n");

    int option;
    scanf("%d", &option);
    flush();

    return option;
}

/*****************************
 * Function Name: dynamicScan
 * Input: char*** pointerToWords (pointer to array of string), int* wordsLen (pointer to int)
 * Output: if scan was successful
 * Function Operation: scans next line from buffer (until \n is received) and uses that to fill *pointerToWords.
 * divides the line into different strings by , and sets wordLen according to the amount of string in *pointerToWords.
 *******************************/
int dynamicScan(char*** pointerToWords, int* wordsLen){

    char** words = (char**) malloc(sizeof(char*));

    if (words == NULL){
        printf("Allocation Issue");
        return 0;
    }

    char ch = 'a';
    int wordIndex = 0;


    while (ch != '\n') {

        char* word = (char *) malloc(sizeof(char));

        if (word == NULL) {
            printf("Allocation Issue");
            return 0; 
        }

        ch = 'a';
        int charIndex = 0;

        while (ch != '\n' && ch != ',') {

            scanf("%c", &ch);

            if (ch == '\n' || ch == ',')
                break;

            char* temp = word;

            word = (char *)realloc(word, sizeof(char) * (charIndex + 2));

            if (word == NULL) {
                printf("Allocation Issue");
                return 0;
            }

            if (temp != word){
                free(temp);
            }

            word[charIndex] = ch;
            word[charIndex + 1] = '\0';
            charIndex++;
        }

        words = (char **) realloc(words, sizeof(char *) * (wordIndex + 1));

        words[wordIndex] = word;
        wordIndex++;

        *wordsLen = wordIndex;
    }

    *pointerToWords = words;
    return 1; 
}

/*****************************
* Function Name: freeDictionary 
* Input: Dictionary 
* Output: None 
* Function Operation: Frees all the pointers the Dictionary uses 
*******************************/
void freeDictionary(Dictionary dictionary){

    Word *word = dictionary.wordList;

    while (word != NULL){

        Word *temp = word->next;

        free(word);
        word = temp;

        free(temp);
    }

    for (int i = 0; i < dictionary.numOfLanguages; i++){
        free(dictionary.languages[i]);
    }
}

/*****************************
* Function Name: freeAll 
* Input:  
* Output: 
* Function Operation: 
*******************************/
void freeAll(Dictionary** dictionariesAddress, int numOfDictionaries){

    for (int i = numOfDictionaries - 1; i >= 0; i--){
        freeDictionary((*dictionariesAddress)[i]);
    }
}

/*****************************
* Function Name: 
* Input: 
* Output: 
* Function Operation: 
*******************************/
Dictionary* createDictionary(){

    int createdDictionarySuccessfully = TRUE;

    Dictionary* dictionary = (Dictionary*) malloc(sizeof(dictionary));

    if (dictionary == NULL){
        createdDictionarySuccessfully = FALSE; 
    }

    printf("Define a new dictionary:\n");

    char **languages = (char**) malloc(sizeof(char*) * 3);

    if (languages == NULL){
        createdDictionarySuccessfully = FALSE;
    }

    int numLanguages;
    createdDictionarySuccessfully = createdDictionarySuccessfully && dynamicScan(&languages, &numLanguages);

    if (createdDictionarySuccessfully){
        printf("The dictionary has been created successfully!\n");

        dictionary->languages = languages;
        dictionary->numOfLanguages = numLanguages;
        dictionary->wordList = NULL;

        return dictionary;

    } else
        printf("The creation of the dictionary has failed!\n");

    return NULL;
}

void printDictionaryLanguages(Dictionary dictionary){

    for (int i = 0; i < dictionary.numOfLanguages; i++){

        if (i == dictionary.numOfLanguages - 1){
            printf("%s", dictionary.languages[i]);

        }else {
            printf("%s,", dictionary.languages[i]);

        }
    }
}

Word* getLastWord(Word *word){

    if (word == NULL){
        return NULL;
    }

    while (word->next != NULL){
        word = word->next;
    }

    return word; 
}

int getDictionary(Dictionary** dictionaries, int numOfDictionaries){

    printf("Choose a dictionary:\n");

    for (int i = 0; i < numOfDictionaries; i++){
        printf("%d. ", i + 1);
        printDictionaryLanguages(*(*dictionaries + i));
        printf("\n");
    }

    int indexOfDict;
    scanf("%d", &indexOfDict);
    flush();

    indexOfDict--;

    return indexOfDict;
}

void addWord(Dictionary** dictionariesAddress, int numOfDictionaries){

    int dictionaryIndex = getDictionary(dictionariesAddress, numOfDictionaries);

    while (dictionaryIndex >= numOfDictionaries || dictionaryIndex < 0){
        printf("Wrong option, try again:");

        dictionaryIndex = getDictionary(dictionariesAddress, numOfDictionaries);
    }

    printf("Enter a word in ");
    printDictionaryLanguages(*(*dictionariesAddress + dictionaryIndex));
    printf(":\n");

    Word *newWord = (Word *)malloc(sizeof(Word));
    Word *lastWord = getLastWord((*dictionariesAddress + dictionaryIndex)->wordList);

    if (lastWord == NULL)
        (*dictionariesAddress + dictionaryIndex)->wordList = newWord;

    else
        lastWord->next = newWord;

    char **translations = (char **) malloc(sizeof(char *) * (*dictionariesAddress + dictionaryIndex)->numOfLanguages);
    int len;

    dynamicScan(&translations, &len);

    if (len < (*dictionariesAddress + dictionaryIndex)->numOfLanguages){
        translations = (char**) realloc(translations, sizeof(char*) * (len + 1));
        translations[len] = (char*) malloc(sizeof(char));
        translations[len][0] = '\0';
    }

    newWord->translations = translations;
    newWord->next = NULL;
}

void removeWord(Dictionary** dictionaries, int numOfDictionaries){

    int dictionaryIndex = getDictionary(dictionaries, numOfDictionaries);

    while (dictionaryIndex >= numOfDictionaries || dictionaryIndex < 0){
        printf("Wrong option, try again:");

        dictionaryIndex = getDictionary(dictionaries, numOfDictionaries);
    }

    printf("Enter a word in %s:\n", (*dictionaries + dictionaryIndex)->languages[0]);

    char **words;
    int len; 

    dynamicScan(&words, &len);

    char* wordToDelete = words[0];

    printf("Are you sure? (y/n)\n");

    char isUserSure;
    scanf("%c", &isUserSure);

    if (isUserSure != 'y'){
        printf("The deletion of the word has been canceled.\n");

    }else {

        int deletedWord = FALSE;
        int deletedFirst = FALSE;
        Word *word = (*dictionaries + dictionaryIndex)->wordList;

        if (word == NULL){
            printf("The deletion of the word has failed!\n");
            return;
        }

        if (!strcmp(word->translations[0], wordToDelete)){
            (*dictionaries + dictionaryIndex)->wordList = word->next;

            deletedFirst = TRUE;
            deletedWord = TRUE;
        
        }
        else {

            while (word != NULL && word->next != NULL) {

                if (!strcmp(word->next->translations[0], wordToDelete)) {

                    Word* temp = word->next;
                    word->next = word->next->next;

                    free(temp);
                    deletedWord = TRUE;
                }

                word = word->next;

            }

        }

        if (deletedFirst)
            free(word);

        if (deletedWord)
            printf("The word has been deleted successfully!\n");

        else
            printf("The deletion of the word has failed!\n");

    }
}

void searchWord(Dictionary** dictionaries, int numOfDictionaries){

    int dictionaryIndex = getDictionary(dictionaries, numOfDictionaries);

    while (dictionaryIndex >= numOfDictionaries || dictionaryIndex < 0){
        printf("Wrong option, try again:");

        dictionaryIndex = getDictionary(dictionaries, numOfDictionaries);
    }

    printf("Enter a word in %s:\n", (*dictionaries + dictionaryIndex)->languages[0]);

    char **words;
    int len; 

    if (!dynamicScan(&words, &len)){
        //TODO
    }

    char* wordToSearch = words[0];
    Word *word = (*dictionaries + dictionaryIndex)->wordList;

    while (word != NULL && strcmp(word->translations[0], wordToSearch)){ 
        word = word->next; 
    }

    if (word == NULL){
        printf("There are no translations for \"%s\" in this dictionary.", wordToSearch);
        
    }else {

        for (int i = 1; i < (*dictionaries + dictionaryIndex)->numOfLanguages; i++){

            // if (word->translations[i][0] == '\0'){

            //     if (i == 0){
            //         printf("There are no translations for \"%s\" in this dictionary.", wordToSearch);
            //     }

            //     break;
            // }

            if (i == 1)
                printf("The translations are:\n" "%s: %s",
                (*dictionaries + dictionaryIndex)->languages[i], word->translations[i]);

            else
                printf(", %s: %s", (*dictionaries + dictionaryIndex)->languages[i], word->translations[i]);
        }
    }

    printf("\n");
}

void  deleteDictionary(Dictionary** dictionaries, int *numOfDictionaries){

    int dictionaryToRemove = getDictionary(dictionaries, *numOfDictionaries);

    while (dictionaryToRemove >= *numOfDictionaries || dictionaryToRemove < 0){
        printf("Wrong option, try again:");

        dictionaryToRemove = getDictionary(dictionaries, *numOfDictionaries);
    }

    printf("Are you sure? (y/n)");

    char ch;
    scanf("%c", &ch);

    if (ch != 'y'){
        printf("The deletion of the dictionary has been canceled.\n");
        return;
    }

    if (dictionaryToRemove >= *numOfDictionaries){
        printf("The deletion of the dictionary has failed!");
        return;
    }

    for (int i = dictionaryToRemove; i < *numOfDictionaries - 1; i++){
        *(*dictionaries + i) = *(*dictionaries + (i + 1));
    }

    *dictionaries = realloc(*dictionaries, sizeof(Dictionary) * (*numOfDictionaries - 1));

    if (dictionaries == NULL){
        printf("The deletion of the dictionary has failed!");
    }

    (*numOfDictionaries)--;
    printf("The dictionary has been deleted successfully!");
}

int main (){

    Dictionary* dictionaries = NULL;
    int numDictionaries = 0; 

    while (1){

        switch (menu()){

            case 1:

                dictionaries = (Dictionary *) realloc(dictionaries, sizeof(Dictionary) * (numDictionaries + 1));
                dictionaries[numDictionaries++] = *createDictionary();
                break;

            case 2: 
                if (numDictionaries == 0){
                    printf("This option is not available right now, try again:");
                    break;
                }

                addWord(&dictionaries, numDictionaries);
                break;
            
            case 3:
                if (numDictionaries == 0){
                    printf("This option is not available right now, try again:");
                    break;
                }
                
                removeWord(&dictionaries, numDictionaries);
                break;
            
            case 4:
                if (numDictionaries == 0){
                    printf("This option is not available right now, try again:");
                    break;
                }

                searchWord(&dictionaries, numDictionaries);
                break;
            
            case 5:
                if (numDictionaries == 0){
                    printf("This option is not available right now, try again:");
                    break;
                }

                deleteDictionary(&dictionaries, &numDictionaries);
                break;

            case 6:
                freeAll(&dictionaries, numDictionaries);
                free(dictionaries);
                printf("Bye!");
                return 0;
            

            default:
                printf("Wrong option, try again:");
                break;
        }
    }
}