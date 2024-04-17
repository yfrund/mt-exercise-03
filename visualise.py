import matplotlib.pyplot as plt
import pandas as pd

def line_chart(perplexities, dropout, type):
    '''
    Creates a line chart of perplexities per dropout rate. Saves it as a .png.
    Args:
        perplexities: list of lists of perplexity values
        dropout: list of dropout values
        type: string specifying perplexity type: training or validation
    '''
    for item, drop in zip(perplexities, dropout):
        x_vals = range(1, len(item)+1) #epochs
        plt.plot(x_vals, item, linestyle='-', label=drop)
    plt.title(f'{type.capitalize()} perplexity')
    plt.xlabel('Epoch')
    plt.ylabel('Perplexity')
    plt.legend()
    plt.grid(True)

    plt.savefig(type+'_perplexity.png')
    plt.clf()


def get_perplexities(file):
    '''
    Args:
        file: log file in tabular format where perplexity is at index 1
    Returns:
        vals: list of perplexities
    '''
    with open(file, 'r') as f:
        lines = f.readlines()
        vals = []
        for line in lines:
            vals.append(round(float(line.split('\t')[1].strip('\n')),2))

    return vals

def tables(perplexities, dropout, type):
    """
    Creates a table with perplexity values per epoch per dropout. Saves it as a .png
    Args:
        perplexities: list of lists of perplexity values
        dropout: list of dropout values
        type: string specifying perplexity type: training or validation
    """
    if type == 'training' or type == 'validation':
        data = {
            type.capitalize()+' perplexity': ['Epoch '+str(i) for i in range(1,41)]
        }
    else:
        data = {
            type.capitalize()+' perplexity': 'Final'
        }

    for item, drop in zip(perplexities, dropout):
        data['Dropout '+drop] = item

    df = pd.DataFrame(data)

    plt.figure()
    plt.table(cellText=df.values, colLabels=df.columns, loc='center')

    plt.axis('off')

    plt.savefig(type+'_perplexity_table.png', bbox_inches='tight', pad_inches=0.05, dpi=500)

def main():
    dropout0_tr, dropout01_tr, dropout03_tr, dropout05_tr, dropout07_tr, dropout09_tr = get_perplexities('models/logs/model0/train.txt'), get_perplexities('models/logs/model01/train.txt'), get_perplexities('models/logs/model03/train.txt'), get_perplexities('models/logs/model05/train.txt'), get_perplexities('models/logs/model07/train.txt'), get_perplexities('models/logs/model09/train.txt')
    dropout0_val, dropout01_val, dropout03_val, dropout05_val, dropout07_val, dropout09_val = get_perplexities('models/logs/model0/valid.txt'), get_perplexities('models/logs/model01/valid.txt'), get_perplexities('models/logs/model03/valid.txt'), get_perplexities('models/logs/model05/valid.txt'), get_perplexities('models/logs/model07/valid.txt'), get_perplexities('models/logs/model09/valid.txt')
    dropout0_test, dropout01_test, dropout03_test, dropout05_test, dropout07_test, dropout09_test = get_perplexities('models/logs/model0/test.txt'), get_perplexities('models/logs/model01/test.txt'), get_perplexities('models/logs/model03/test.txt'), get_perplexities('models/logs/model05/test.txt'), get_perplexities('models/logs/model07/test.txt'), get_perplexities('models/logs/model09/test.txt')

    line_chart([dropout0_tr, dropout01_tr, dropout03_tr, dropout05_tr, dropout07_tr, dropout09_tr],
               ['0','0.1','0.3','0.5', '0.7', '0.9'], 'training')
    line_chart([dropout0_val, dropout01_val, dropout03_val, dropout05_val, dropout07_val, dropout09_val],
               ['0', '0.1', '0.3', '0.5', '0.7', '0.9'], 'validation')

    tables([dropout0_tr, dropout01_tr, dropout03_tr, dropout05_tr, dropout07_tr, dropout09_tr],
               ['0', '0.1', '0.3', '0.5', '0.7', '0.9'], 'training')
    tables([dropout0_val, dropout01_val, dropout03_val, dropout05_val, dropout07_val, dropout09_val],
               ['0', '0.1', '0.3', '0.5', '0.7', '0.9'], 'validation')
    tables([dropout0_test, dropout01_test, dropout03_test, dropout05_test, dropout07_test, dropout09_test],
           ['0', '0.1', '0.3', '0.5', '0.7', '0.9'], 'testing')

if __name__ == '__main__':
    main()