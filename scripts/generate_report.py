import pandas as pd
import datapane as dp
import seaborn as sns
import matplotlib.pyplot as plt


def report():
    df = pd.read_csv('Advertising.csv')

    df.head()
    # histogram

    histogram = df.hist()

    # boxplot

    boxplot = df.boxplot(column=['TV', 'Radio', 'Newspaper'])

    # Regression Plots
    scat1 = sns.regplot(x="Sales", y="TV", data=df)

    scat2 = sns.regplot(x="Sales", y="Radio", data=df)

    scat3 = sns.regplot(x="Sales", y="Newspaper", data=df)

    plot(x, y)

    plt.show()
    plt.savefig('foo.png', bbox_inches='tight')
    plt.savefig('foo.pdf')
    # report = dp.Report(
    #
    #     dp.Markdown("Advertisement Report With Sales Data"),
    #
    #     dp.Table(df),
    #
    #     dp.Markdown("Histogram Of all Attributes"),
    #
    #     dp.Plot(histogram),
    #
    #     dp.Markdown("Box Plot of the Feature Variable"),
    #     dp.Plot(boxplot),
    #
    #     dp.Markdown('Regression Plots for all features against target variable'),
    #
    #     dp.Plot(scat1),
    #
    #     dp.Plot(scat2),
    #
    #     dp.Plot(scat3))
    #
    # report.save(path='D:\\projects\\FAS\\templates\\adver_data.html')
    return "success"


print(report())
