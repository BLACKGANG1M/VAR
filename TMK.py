# Encoded By TAMIM

# https://github.com/BLACKGANG1M

import marshal, base64, zlib
exec(marshal.loads(zlib.decompres.b64decode(b'eJzsvWt4XMd1INhPdONFNF4kKIp08yWSogD0fXX3BUmJIB4kRAAkAZAEwQfYwG0ATQIN8HaDjxYg07PKhvLIGyqx1lQsfoG9ZiIl5hfmwR1l19yRN2ZGnohJt9KMuJ3FrDf5vDPamd2PmtgTffi155yqe/sBkBBt+ZEdA9V16tat56lTp06dU139D5acPweH//gshL5mGbVolm9aByyaVbONWwesAO3j1gnbgM2KcY5x+4RjwGHNfW8bdw44CRYNFBF0DbgIugfcBIsHigmWDJQQLB0ozUtXNlBGsHyg3GYJr9Ccv2u1WP7AajTRailm9VUMVOTV6xnw5JVbOVBJsGqgKq9eo/zqgWqARePVfViea7xiomaghvriHq+dWDmwymqJbt9oCddtsugbrRZoi/XMaqMVWnFhqwrelxS+P2aJOi5YLtqPWS5YAa+lgNentLJXLANrtHLwn4b8VWfWGukhxYpvWvPLGFi3KE3FojRf0DxQmlerHFivVQ1sKGbt2mi8D2/Qqr9d87s2yGPLti3q2shaaDfaN7AJPps1a+gZrXZgi7ZyYKu2amCbVjfwrLZ6YLv21MBz2pqBenhu0J4eaNTWDvi0dQOC9oUBUfMOSNr6AVnbMKBoGwf82iZoT0DbDH6wAEfPFOJI2zKnWpb4G7WEt3zd8rpV2/q6lYe2QehZCj1rxm03454z4+rNuAYz1AihrRTymSHBfCuacZIZJ5txihnn/4x5A0vkDZpx6uuFI9ikNQGudmg7wN+p7QR/l7YL/Oe158F/QXsB/N3abvCbtWbw92h7wG/RWsBvBQzv/F0o5Q8sOVi19VqAjivOtBlxZ9qNENB2BdHuCq11McVizvBeSFM6sA+fBvYd34dxLHTBatDztrZtbyxU9HbV71VFX/tMd0+r6utKrICIPkVSZjp7+kVx7wI9i5Iws/9An6zuowwvSpihs+uYHDiyULG3r75DFVSfmQIiugOCz4xgRfqhiL7DQfmgXgQN5dkUSEUVtegOiqXmSGZzWKwH61QEX3v3THdXu+jvT2DugwrW0dHVGZD389xYc9AHsS8OHFDk/bxmaDzrTKKi9+C++s6AaDQtscJsxYuthyTVqF8x63dBuQmzGN4hj4GDbhMJENMMxbTPdHXtEdUuSkIRh3mMXoEtpJIkwShJL4NIaru+wggtsL6JQraRbAjyEIwYF40EZSyBQs8cvWaDWNepenqVyA45tWy/XoKvSs1GrDASYf59RodYpRJiqrdXUF7U3ZisPI8aWEkV+UPBe+rKVo2t4i3HZL0BSTVGjDCQM7o81oPlFqNHNWBZ+kr0EH+JHPLguC4xkEkDDEUJxgB7eDeEDqNhNUbZDI3G4BjDkO3BKqMH2OEuPvLUAjasQSArTjXV2c4iLTE8s3YGfIJBXDs4+ZmtYahHnPYJ0AxqMaGTSCBnBjCSCPiMWarbTJznoM3srK/DmHprTMytNIZKd5p4zcWYMSVYlqfMLG6TTioMsuHdz7bGbmQx0bXPQJfdHMlyc2ZJJqmzKqhGm9EqKiOnrzsYeUg0pow8qs1ZZDPIh5FqR1dXwN/KR0Ip4CqVhVxlB2tuzggx4qA2V5r9rkLvaRMXdeghbei1xhRj03q1OZiSoHBkOgyEczSLIkcz5zGikjfpFcXEKY3SWhPvRGFluUNFLfwYF4HubdaMYyoUH0N4EGBCXXNcCu5Qdgiqf2IrD8vBiZdzordlo72tzT37vUcP9HS2eqEI67Pg2UNTEQBVfWN6OKQdnJwcb7sYHp6OT+qJ7VORKW8kGouHxse9evjcdDgWj3lHpuPTeji2a5fofd7bqIXPN0anx8cT5VOX4mOTUW9XT1fD1KWt/w4GLFEtSGqDEBAaBL/YIPiaFJh1iWpZaRDFYAMAQQ40SYpP8CWqxECDDGn8EO9v8guSL5ioEYIy5A7CB94EmwRFDEJKyd+gCg2iT2qAxatJ8QeCiSoZqlH8DRKkFf08Tgk2SDI6IehvEnzAsqBEFUoSoD2SQiUGYYYmakRRbhAFCWr3Q36pCcqVErXUdhmyQ+GiDImB5/kTK4BvNECP1ECD0ITNwbapCtbj9zWJwPEE6DY0DhsN5QpGG6vxWfBB16F6NdAkC7KSqBJEKE1tkLBJEpQXlHIbGYBioZEBv5LwYLfFBrUh4G+SVRnxSLX4EZlQEe91jQxd8CHC4Z0A2BV8WLcoiFgNYAGQJmM9mD8HvQpgV/JJiQrof4MCfWsIQI8F6IvogxpkaCVE+mXWbMgKIyCqhHCohXVQgCTQSiGIuPXx9lBnYCgEKMUHqPAFA4FEpaAGG4IqjqMs8uFivREa/DiGNF6JSiwJxgVqzkuGYwJvJJ6sBrMEIXcQECEFm5SAKkqJSqgOO0uDAM1WJE5Q2HQhgGPBOlODA0ODAm1XkCBVnwwV+QMNQYZztUnyKTIUCU1WiHBVQISkKiIjZqQxoArBZ7QbeocUL+I7A2OAKmynT8Xuiaoii4ka6L8g8sGCWvxQjZ9jgsa0QeHZKwGvUHkQh0I1MKuoNAskqFlQm2DqBGWg2gDRMHQP2yAA9dBYA2XL2E0Zhw3K9AfURCVUgC2FVihBA72qD9CL00kU+dSslAOIBZgCgA+jbkAijgzgUZAQFzKgp6CPfkkkCkf6AbqDmQS9oeyVQsDXAEMBY6bIxuyQsRfIESC1ykdGAAwGcMrgcMl8EjP8QKlAlAKfR9XEDrAmInKjlT6Zmo30JwaaRGSokD2INKo24GQPMsKoRNJVJaJxH4uqUqBe4BLQc7/SJImUFbEVhK5AMsVnToXsLDJGG6ge24E8D2lX4UmxSEVBpOEgsDIrsddYEbxUjNzAeSghNEmUpaaAX0TiBYIMCDSwIjIpP3QUsgOyAwoObhAGzC+qwCkCOIOJHXLk4myBgRVkpHKJEWktxiBDEkRso9TkV2QfTE3ohoTo9sNQmsiF3kgNOD8CQpOkqqKQy/ckBfmeH9mrwKcS8jODJVUjdkRkogJyZD42hF4oEIZHBCKQBL+q5nN8EXmSqCJ/ppnsJ2pHzsIGiE13olU5wOOQYUBWGFosFHCjQvUKLSs4HyV/kyTRfFAlhhEJpzN2MxiAlMjUAXWQFxtKna8ldoZEKCHVAWUGlICcy6RVnOsmMSAPAb5IeJZhvZMxUiVU4dRU+eytxfyiIjYQbhXoqgypGR0LUL0oEQJYr7DrSA5BnL0mX1WJA2NbBVE1RkqQaLIB8hsMFlyJCJVpZvoFo52yRMuLAMMcMLgWURYyfhxRvjwBXVFrBCQmg5OpxEiAwLDjKpADFhjgqIDU/qaA5BMZ0yLECwGlKQCyOhS4KDMt3lgBzmYgWCXop7VNRjKkddqcP4hZP6ILVwpApOL346AZU00GXsFSeqCvOFWg6X4jL8w6mc1HHAMhoPrZfIbJg9Sq8ko8uQtgEP4MZoe8PGjKEgzVEhtDwaBqjyBDN2Q2+kFZBuoLBlnrkLAVv8FuaN0M4vJprGGYiJYln5JdUmuQxnFRFEWkKxBM/ApOKJy5NMbI6+CdyqUBnHvYaUXFUjElEC82BynQ4A+VSPfIxXxIDxQFZCcydhoweghrAQ4nIlWlIQhSHGIbV3PojinDAHfx+1CmwQnaFIS5hFPWRzij6SQIJmMTGH8QMb25mEAMshwcG5q1Ph9RI7RbRhQH+IwnNgaCI0hKtEYwxCFvx8HB9Q5SsjWikEih8SJjRLQWQG1+gzcCQSGCaf0GPuSH0WbzA3FCeOdMvUoRcMWiFdPXJAUVFZky9hEZKAkQRpm08GCJQBySz5hLQL1BXLKBs8J095PkCa1GJk+UpRhSql+gRZnWQ8lc9lAAVIi1AbNmSzPnl0ANJEybMxTxgcMukHzFSAFlZuRXMMSQmo17FVuqYe2AFyA3KchtchY5ScxZkZh8RE0DMc6HkxkWbZjvSBMB1eglkGGQJCdcAJYQu3x+k1cFqDc+P82MrJCMqEToMxCPUwWplZYQmJTINJDTQj0wj00ZwgNSeQOuksDm/T45SOsJzkUZcSzgashXvmCA8CMqhHoQX3yCQnIOzWZaY4LImipJ7hGoIjlHoGWMO4iUCRwSSAtFKVzKYIyMtQhI0M/kI5XWa1kVFDZ1CYl+mtBGyly5CaTBoJ91ENcj6I+xpanMrrmyueKY7M9PUilJi/k9kaEnHoXxUhoVIFQh4cHlE2gUxkVZJLbixsFPTaPVgFMNZyA1uECRXC6QzGvSYpCtqSiBGuiqJo6L5AVEHTSXnwJBEXCILANTAi0zRg7iiCSiPCsxQQHZEIq5sl+VmcCGsguIEZxKoIe440Nmx7mnB0kYqlBopJtohc+rWILqENN5kQEfbFCqaH8RQOqGbRn0ikhORTajIgcQeRW4bYXpx1h0E8gpAYltbkRkXiCcIGZhnjOcqCSBoRTClpD89nG+hx3F7RY0APfBfjFnFfabTDdf7PQb0xTXABwcP9Kdz1haEIW0oVBQ2AHSw1bizIBeoxjuN/grsQbimT7cHDNWaGBHoV2w6IcWIe3geKD8IdM22BMk1Ai4PKNAoRIKgeeotK1ukmTgLkgNIqXDYQoYHJxWDqBpJcjISQz4A3xthimGGVCSwyLzKwmy3NAz4r60EINYDUsEZ0MoofHdBAmHebmlgMr3EiL2G5Oz9hR0hXbaxrqFRcq8OJw8MO0lH99KIgb5BAXyxyUyd1Rw56/SFlgCwpCyuyoRx4QaXcPWJ7Y6C6ieQLKrNEdfbTDWUZrfKL2SaIaUw0QIlWgkSJIydDAYIEbpo9UEuLxiiM7QbOSnPrZXEml9kJksi+UiuzJnULaRuMerMqtWGoK84tolVgdcHmgEfShMYSMZZ6KNPzAqWqs5JdPcCDbg+OG2iAQSYtEYAz1XTYlfYQQqkIADLcT9LqIaJV5iCDIwfjUoM5rCBVeQfFnxzNxCUV9xLyDSBgHGB8kUeZxoLuEotqrEBEAQBA6lAk2ilIICgR9li9zFzZiIpKRSUebPjgVQvxyUA7hewjAESNOE2yjojZ/JtDjFsLMoZeGcq+UsFBoqsykhBURcZNQGH8M+yE6qD0TsGpaVaWiwIh9sxJCQmMioIn1IyJdgRtUYAogYJH4jBaHJiSpUIAmk5EL5JZjPMaDDKGyA2BmAeYGtpw1OzjqTJQ9VNXdwfK0XjAWpQESUUQ24iC3Jkl9mjSSdlsI0FWogIC7CEkn+RIrAY5FtUBzun7j6SyR6alKCAZ/M1AgCp29UvVH2Sj4vAHGyoaKj5UtgQoRg6Bb5XkJmLDWXZgO0e5B9Rm6m0cL9IiBdAg+QljdmCu6KAhKpyHCHDeOLzLOSIU1BoV40JgryWyQBcx+XXxTtnHDdgYlIuAKKElXSKKKWkHbgfmTNgpCrjlBoGTd0j7kpJfhDspdwPULhA2oy0UICOq4CKAOIfjGAQhntFRB/xkpTOEyQGacX518ouauGSAfjREukkFXtMT6JMjsmVjifZGIF7ipFkTb6bM1ARRaq3VBnjJoq5ESMc0u0LAlEj5zIZLbg4N5ZDjKphrSuyM6R69NIGcQs4R6TMeRKVFPRUoxrtrEjk1hzUL6WVZww2EeQhJEBCTm63UpzrwQLYe5SgG1B1hb0GWpOH266sT/EzGl3SQslbaFwEskK8TpSDAZIQkJVBMxiMZAvChgKsUq29BLezH1agEm8AlNVm/XIbMVRAT0gICPKaUr5GpiGSDAF32ADIyTSWsJmVAwwlqoyVAoiqTECSq4kKRjifpBwiahDNTL20lCUI5ML4nbLoKJ8cTgoqbSnAU4qET8HclOC0HwkLUA7KlVw8wiCjc+Hq4SP7epJ7wvULaHmTSCBinbRsHcLQF8KjAEBMgbA9MTNHGAdBknlLL6W1lnS0yCiA6R/X4TPoAqEgHtEifgFScCkz2eypEgNIDWtn5RXWC+yXHN5qzT4M+ymJMaIPYZe0t9ginh5eidDT8O36qi3gHWVlgbT3oDo8Bnrb94MoSaTLh8jkNhFXOQVUoUZ1cgNgsn1MJJJsGTNYdolgS3f0BPFiCIFrUhrZVMABHbWGNzoBdFy0uQHDBqyBLzAVsvGlPPjjgTLD/BZXW1IVCrJVJIsU1tEtmnHZUUUl9xIAS8RcO1AzYAUMMXaRbYPQz1RhTSMTcftpsikrwKTgaHNx2kj8M2rohrbT5QjIDWgwqjF3LzALAOy8UtC4RAg+6g1l0KBLVCiH60kZLUJso0ETdiAtLiPPkVCqsBl2ceSslaSvGQOIpCB0UeVxJoA0zJl9+wCIjJgqowrc/eL0A7cPBGvYMY3FE5FNHVVIYlh5dADWTREopwtsj9AW+QAGzGJ2XgEE5HEHBXOVyRDYwvtwV0VriaGuaOW+L9f4SYdqkrOFzJlQwvKBlHAhSyIQoBPkth6pRKTgpQm2w4wYZv0cYwCc0lVMFQQtWwV8vNFRyb9jZK3ITclXKgH9SJoi0ALmsCqzkb5fSTR0KZHJDWLodStyrEb4RJERhpsC6xygDlZMcjKyEvrJd+1MJsjcJMGU++ez0eVIEo9eW0hQaiWdk+Syk1GwFJIkMhPGQgYmlBihIQfvhZXmcuSZHIFJkmJTFyRzG2/yDSwOCNMXRnX+GB/YFXMURCQgIHcJsD0sAVohD2GwnZm3GoIIyApqozCtz9I4gbJ6Vw9Ucv0iWxbTzJ1AJYqrrEX2MZeUQ1OnFuT7AOGXenHfQjbqoMU4ZNhZHA5UlDnBMzLL0vIaxjhkKEO9QY+ts5wcw5tSVD1R71BqgeiCjKphqvjSJUnkyrcFBlQupaJ9JEcxYCK+iZOKbDpysNZjlKFNurVrEQ/bfNVAxUmXxCZahfwpcrM9ocYQl5J1iCVzU9sPzJPydTHyWwW42guVk0pXA3JFInMjB0051GuCAMMSAwAY03UMCyQ4dLQgy414EBsIEMgd8E1I6gYxJZvfKClsxJ3kMjpaD/LTPWML8iItRwrWO56iroeGFzDOMZoS0RVEawlWChuR2l8JCnXrM8MZsARjfVBQssHW6MQvzD3UBZluEQND63cioimcJHZVtESZS5j3BiKGwrcGEkqn/RoLQuSsMLkJ0SNj4nGAYUPb7XJfuFV0CAjQxrg5grZL+Bui7ZLCtsXiNh5WKJyF/+AaQoyzc10sAA6D1zMl6OSV7gOiwmVPlrUBSarBQI+MWcboOZwakN9pjB5lvRnVaYpmOSqHJYO/cHNhWTad3PXZjE3KZIc66ikBqHMaonplMl0oEgGnhWybjATsXFsJEgcjsR7FMMY51F9ZH5X6YAA1yapOBQS01MrdO6jRhHYWOAxCxB8gfkJJGf62FYDuRJUI7LxBDFa4fZ/WTCMzrAFUHGRRU2WLKtCsECPBhtPJZBlubhbM1SRhjVfpD0/j8MGSTiDBCVo6q1MW4/KFSPmIgP8SDG4Oi5EqFsLkO6pyZDMkQ79zDgsKsHgIvOP6oNdr0pGNbbG4LEdsl74qb1YlhT0BYRCjiUHghJZCPlRDNwtmIKMQoY/iURo1mTMyOzXfoMvIUvFnglkxjcWJ5VUIVB/gItlVUQvuJeA4YNJI5OaDAkBBQbalAcCKH+RBoari4KmSZQWaAkb/ggLGMiPOEQ5EqYh7SgUw8iVxFtBNY7xBIn5qVwSqOQCPVIcCCZssw+rFHBjLNZvHqQAJodHgrhOhozFeTmBF8qk20Ptuoj0CRybLCimCVwmKQkyC0qigg0TdNzgrYhT5NXYP9nH5AC2ewG6gOYEsjYvEWkX7QKwlptiQFYCBcIK0MaEllyVb+A5VTKJmvbkZHtXZMnH1kN2TgQ1sYZU46ODEYguU7FHQgluN2BO4P5CAK6Kkr+IG2uiWgNlWcM736uDhCkK+Zpbf64gKRLr8GePyKBlTqHzUDT1jNzG2S7ROARi6puJE8JI+NQc+5aQ1SZ5cN1CjYmY3eUZe1iJFOxsF0tGJhgHZEZZjRUKSkyeB+JhOzpiqX6qWVGQ/xKNiuyoBOIiYGh7zOEJNhhnCKrYyTpKbGiACrpiHOtQSZrDFcVnzNT8hCou2Waf/TSyfp8/QBaRHI0JEIGqoDSWhx4lO2uCzNgg0AEkWKGR8gU81BDwMQNrgXkYh9DY6AVZcwJ8p03opaNLfjbisrKU1KcqpEzDFYIRkXnCjtgVGhZQ9yRzpQVybto+IkcPMGN5jhaEDrgoMlNjoAKIppXRwYJVOOgT+Zojkq4ZGxhQgMw8+QIRbaElJhQwfaUckHzmLkKl42MgofkXSbTAobho52dKA8gc8AtyQTrYvxWqlwzNr4A6ZxSGGtAoqJDYQWcVaOxQpQfJ1MLtBorsDH+0dw6Qbd5Q+AfJlowj45MNyxBE4izAwy+CKb6aO0HSIPr4TrCWHTmgrQVFSwEfnUwx57vfNEDS4QI/0Z9qChOGpKyQmkAKCExPQ5Ican8VU8vAJUsUY2U/U7FWkjVIwGVAkoxtMDwjm0OtEVqZVeixsTMiAghgI0WfoYMB/o7T2CfmSJbGRtRkKqSL9bNDe8Yqj0xbJtzjSSouBOKo+RQ2G5rkIAiwBfTjl/38iJzErQ14DAlYJ2n6oTRcOHOHh5iFj3Q1TG+J2GJ7QdSBw+gmKlRiYyhDmdzEx9qBB+n4qsWkA5w+qmrsfLi1G2Q+c2eIuhS0B9Nybkh3dFgNN1J4MhBkKQXP8TBqCDAds0/kwj5uCcl47SNVUK6qi3Ypkk8mgQOG088MO8amK59sJVq1UIXIZEURjWayQsclIS+JgDnnMtnBD5Wdzwkay3JOiaibhjLZlp2MjyISlyAWnpQw9FL5eUmrzo5Q+hromAhfRqg+aJ55praAo/lUiW+LoF6feaqgOr94SZKZUllBGQIlRzz/iLvlHMUOUouPVAoyilMS5idB09xBG0bLnDUNd/gym9CovwkIJAPmVQ7jjHI0s54Fme5Syh74Mw67BI2jktV52xpTn5VVSRqrVQEOJVyYakglQNZSMatoqsYFiG1w6cAyI3WUSEV2Ts3UZnCGga8M1RdZUUFSDTBTCSy9AdTOomAksqPkxgFEw6pEx9lgfvrxJIKpjSerIT/ChefR/MzW7pO44goFOZgBQTpMAoK4RGYuOuGr0nEoVD8zSzjT/4q41/BzvXklHZ1UyOppnOhGc6fADeYwv0WQa5CpocJMJquMQFsAnPM40+iIKGvhIvU4oF9S2YaRBAwUimRz6ZWYiEBnOmVTqENpQCGZTBRFQ1cg8wOquBtQ0YxJGoACivFj1+mMmkRWQ1QiQc8DPq5s8BknL/xcZcm0fmjRV7OHAxjJYTdF4suKSEeCskupbA57fvUCnXzm8jAKM6hEkhTBzxkB4Yukl6YgHWZlOkey2KEACTM94OcqFR/blRjSJ64dZOMUiNUJ+PWD/CkdFASDjHGiklVRKNCFk5kRxw71LNnTOMHsucoqbJIfFdk5ky1XeWPyXpTtgVnRePtyZqCpvzMOUaJ6hx/IliXaOsrsLCAJ6cBQ/AKeISYGSIdlRNHUdwUNIycd7zHUNHl6I2SWwE5Y1+mMnsAmsOoL+mH3SdQOc9BvHrgMMmO4iow2yDaGfC1AAQ2YkYRfS0BSJ0O4aswLkobJ2CtmjwyqjElLzAIowxYLOigFuCmV7VFVSaa1BYeFDrHInNI83GxN8wo2aEQS7PwWHd7FRV1VfHyxQtW/sfzjsPhpXaCqYVWDnbXELVZ0dFcwJIIclhwwT+H5JKbmpW2EIc36yYDKpyNaqAU8Ihqkr3agBOnDwwsS337iCOBqaZwpNOJQbKGTmxTJj1Pg92RgkRVpD0Bf2+Bf0xDMU/LUItSKsEWGktbkGeGV7DkyfqQSFnTZbxrJJdKNKA3GsSE6To9zjszXOTpHicmWIupaKWU1OznCFHWC37AIAL9BRk1H2zj/rlH5CXDkhnh8IIiLIe3GAmTWU8yvIQlk8KWDitnzgoyhiySa+o1dKG2yDMMHDiUdaSDDK+lrYCUFboamMzq9IPrJagRMPYiKv8IzU3yhkcmqQ2JQ0DxzS0cxmQAmKua+EdidyuR61KeREMYahVNPodOvUEAQD1EWbE9kxfyyB1IOylKK0QBukUPsQXY/TAKOftqB0SFtIykjBT5hcLWT2RFZeCRND1CTGECWxZdYWkZUs6fs6BxxV2Qwqq+QNQIh54ghpgm+klggiAtqMPt9C5zjKm+J0cAaUjLgrFTp5JTkl0ito5D6F7c/PoV/kYoIQyErtiAoBscKBLitih12koBLSqQnBw6DTAbtTT4JCUlhSjZY7lSZH1vgOiHaKgqcOlisrHKFjPmlJiRNrB3nFykaaOtkHsWgsy9QbBC/tMGO+2KbVH7IAY+VBJh6U2RneEjng4RFK5qQa18KcptVk9FthUQBnBWSEoQNRTWtwmjB5trwIFoh6HsnPn5ED6aln9S8KlkNkXeYR9NxAgXoO3vGd8CqcEaSOKWax/tJmysxw71onLetZHsd1c8PQpssT2HfDcCjXUwlYCwwQTpmYuCWuI7MxQi/8RU5OsUUpBVOMk58ZS1JMjNcs0Ox+O23IDufhlYRJSCQWktg39uQ8Gs6uQddJB99M8IUSwy5hqa7Siof3CzK7DwRW0i5XomPN2rfuMq9gmhVRv2qX2FHioCYEeOEXL5sCVxxptCCwjdeRq30bQCqlYkoqC/E3hsnkqpROAqIbHBQjSNIkjmySBV4oA6kRj/DGhofUHQiVTSs9bjpCxr7YW5pJSZGmhRSSxqcielmcCAFY5Uq+KKc7MMvGVQiA8PZLWCnDXWvSKpPppYPKGROJlMK249JxgZFZAwwKJt5q3NQgedbBNZB2nw20KYdzS7I+9gA+uiwRfYLnkxyEZg5RpTYyAybFzhY2HUu+JXjf3zXgte5zFg0awJCrZaTvbPWeE7CM2auOZtlib8Za+HlEI/IbV8qd+GFFPHinLxOI6TZCut4rU+z9Fq22bsXrCWj/+nQu+t+7T/+0QvbijL22KVYpigW1yan4xnnBT0SD2ecI+PTsbGMIx6ZgIfYeDg8tc2WsU5krBdj2CWvN1PcNx2fHj8biY5m7BcnL+qNEI3fEo+dAO+y5UH5iqs1r/Y/tNidq8m7Yp13l75W8pG77kN33bXKlHtN2r0m6V6TE5tyP5V2P5V0PzXvLnut5Kqcctel3XVJcg9dRkH/iN3JGxi7MTCbaGDiOe9mLItuRQEkvGPFr2I7p/RINL7NqtdjszGJV28AP2Od0mWA+FXyWCX1Zt5RfGX9l/a9su8y/es+iN36LGRZcBuXNmSK+EUdLn5RR6aI39Th4jd1ZIr4PRFu43IGSMKuqXAbd3XoeGMLPdJNHezRxe/pgALYbQG7IDabku7J4LW16E34bofFbJrka9f9GJd9UWx+wR4aTd+wp3LoG+uZIn5xR045xpURmSJ+fwHvoqAH4H3CbVzeQU3SdyMKnexWB7dx1QJrwvPovYBeh9mDYvPOjmyr6YKMTBG/4aLYvLJD78ZsXeh1m4iRBIFVTGUG8rqqd5qh/P7QPR6ULcGHx5eLUBAa8l4qGQfdA2EinjUikNecnLcK4qCIX+PRgjGt6O1Fb19+u8xQwuj5PtY5t3FbAqCd3eyBmNWbjc5kHHS1R7b0bEP2mg0xMZ5wG1d8sI65jQs+WHuyGGsz23jALG8PejSC2dqyY5mtLTsCLWbebA6zjoTbuPxDf5FIwLxtoxC32YoPotebM3x8cuj9Ru0JY1p1sY6YjWFkEgT6pJJ6zObuR6/PIDq6XyLh4leAsHJ780fIxW8AoWbn4LuFhgOnEqsr4FNY+xWj/WwS4QQj3Jpd9nUwHA4ugc1sKFvTTjNuCbyysXsxv7xT5nhmy8sSUpYOC6hnXxZxRmeCZn6zTBPn+1gh2STZkdtvhBJ8uvoKu5dtrImvnO6dpKzGHSNu444R1qfsYGaxkC3kMI5LEb9sxG1cNlLADqmqBRe/akQ/bubOkmG2WwfNUBZzh8y402aOLIaPmW9NSqV26UfQy7KM7NwZKESYwsY022KTCvhMAmmNkvC1R1RymJei8OErIJ2h/EHPIhKJKGPHi0vMzm6ryDiHY4MtAxlnODq4dw+Bw70Z53h8sLMPFtLxwYOdGWdEG+xozTj16cGewxAZHzwI78bCgx3wbiwy2NGdcUbHB7s7E0XeSHywo4+KwdhwbLCtl54O7h+25PyhrEErO6LjayBw5QpKKHxpNvTjtoJYO/qzsPqDwOPoThw/3r6nubuxfY/cvANCRxoVPItP8jVIzBC150gjMBQ1ADtVeGrtanxJC0djkfilXVKD77kLES0+tgvlwefGwpHRsfguWB98s5Cys6Ux0QGwpaexo7vVG4ro8fA4PHe1N/aGJmLT0VEsvDXn4WB34/DkRMNIaDg8NDl5tuFsKB6KhrDSI42JZwH2QutQvb8Dr2WBkpsbQ/pEODQUqT8fCDXx8I6TII45sH70W4+ANGObDuXKMLbwRf08BNbDJ4ZjCCKZI3R/aCTlGHlosYxZY7ZPLBZnzPZjRN9FerhogzeXbGE7PoTtl6t+4C65vJqEncRfFaLQLxgo9KsGBgNyELYnBRgUTAz6fSYC1YCf4w/GvrOZobDrwJGO3r7mHobAnsnhs8NjkSmGwf1KvbR3GfwZaQiFsN3IovBi0N+Ug8YdJxOljTFtOKRrjX1d+/sAfe7wxUgsPjh5dsG15riwQw1MJEpzbuFJUKwkTSRKsvfxJIp5OJgT7c8JB3LCajas+Izy5GykIOfUKEq5D2I2VdCf+0KYyJst5gZFthTKwbkz5Oswj64v2h7Q5sDWvSDWP/HfNpsuIc1Ze96xELUwEnSOR6JAhbMQRo4T+wJR4by7/I3K5Ip25lLuvWn33qThKHden0zZ/siiPmU3StriDZUzmy5elA0/otfA3sbDIX2bI2ObxM3QpVg8PME65RifHJ3UZ7BXZtf0LxoeMsvYet6xkteKr27N2diUf0V7tfS10iv0z6ZR/UVttH5yKhz1jsXjU7GmxsYLoYaJcONEOBYLjYYb5d4X2/Yd7Reltt59B4QM8PASL/0lpL7cP29vb6+X//Xin/cw/OETQTPTxS0AML3Xe/qi93R/fwPP1NDc3LzFexp8fGg7COmMTCIBlgn/+vv791CgdQsEAR7obPN2HsaSsxUV5OnFXA3ehl7KDhHN+5r37etnLx+Vqc2LLezf4jUy9R4+fLp531DD4zJRmYeNhqLf24/l9GI2I9Mt9C9Cpov0fPHYRQN5CciUAL8XfAP84v9KEtKTT8OSH+NE+fvrf7xgfZkH/yRR6m1tO9LWeeBgW493wdqUWOHta+7q6PJ2dfQMNEM9pd4jbT29HQe6odaE0+trkEr0ROEkXGFMwn9nL5yEi7QROTqL3El4xr50jvwJOQtTec5hWeKvcCM/ay22xEtzyjcneaHm44zLzGObsc7Yzlv0WLwyp5VV2TCwRnu8Ju/ZUfDeWfC+6Lp7EfP56XBgj6/KyVNm9su1qJ412XSLrikFxvY59tJd8L644H3J9bIZ0oZppYlFPYKWrs2mXkQxn18ry5YYi8fV/IXPrebyxTVrKxhGZh15NOAxQlrFjGNJXC09+p5F6TZm0y01+ngJcXxzTlmVj0p9jNLzy2cruxes9YkXjOVJD11oGI3Ex6aHpmNhfXgyGg9H4w0ggjXu6Wxu2b+3uXuv0NV4pLmncSIUiTb27d8caDsbvqS/YkGBQND/W4CJGuDkLS1tvb3thzu9zQcP9hw40tw5yqr/wQuJEu+xyWnduz98yav/OqYvwmsIdx1POE7u6m9NVHv7xiIxb0fMezAU0bx9k5Pj3sRWb8t4ZPistw0apEOctxfaRUU0axORqPfoWCgea56a8iba9oXHxyc3i77eiA7++s1iB4CjoWgcQB++2DN9CYNQCcVMjiPswjgoD/wm+CS2hya8sXhIjxes3NvRoqdIATEQVH3KC/Hwxfiuj3GYtlWThJCxx+K6fhlDrtFwPDwd0TKOM5ORaMZt3MmYscOLjAOzksyhv0TI26s/iw/bqRAQU0mSgl1WdGo6rn8Jww4QWuP6M1iZM+OYxqJt8HFjC1tCY/GMfSI2mrHHz8ZiSIK0tDDZzB2amtInz4fG9a/DI+5RY39jJSnG5vrSlle2XN4yX1z2lZ7XBl498dqJVPFT6eKnLm964Cr59Yv/4uJVx5defuXlyxse2qrsFfMVq16bST59MlVxKo1u+PK+B67iK/2XX7788nxR6VfOJcv84N44xOD1Sg55PLhUUSBdFEgWBebLKt6wfbXk9bKvlqXK1qbL1l4eni8qeeXM1eovTb4yeXlyvqj4S+FXwpfDD4pKLms/ZIWr4LBwhFg4QR5/s5nB21YGwb27IVW2890jqbKWVFFruqg1WdQKrfzS6Cujl0d5cxVwWCJCLJEgjweXKvKni/zJIn9hvhfBYT6EmI8gjweXKtqfLtqfLNr/oLwvefhoqvzo5eH7x46njw09RAH2EO69emyHcSOmWQkMWI/YfsTAQwYYOiq/NPHKxOUJePjSyCsjl+n/04c2KwyGw/XKvi+9+MqLl/n/p59+GkNG9V3nnhV7ayx/XtuyC8C/qand+5x96RU+7nqiFT5nrcZtRa6oDc+2gvf2gveOZdbOx5fuXKb05Vbmx5fuWqZ09xKl51hiFmEtR1ZZpubiZWouKXhfWvC+7HpZoVQ1A2NxlraAuide/uhW4joAaZ0s7VWb/nlRQvkyfVrxU41VxTKle36q0iuXKb3qnxElWGesWjmnhBXxike3EtJVmOkqH5uukqeriFc/Ol108LE4+eyjUb0MTmqWGI3abIozJva12kXpVmfTLWrhU9l32kpzLj0mB0ngP58+r/rZ9JlzA6O3XT+n3tQ9mRT/c8Tzz4i2SAm1upvLzM1MZi73tnd0tnlbOg90d3TvzVj3JCq8Pc3drQe6snFtsH1vAxGQZOLYgvWFhVKQg8fDw/HIZJTJ0gtWr/5lLK/Uu6c1m1NMrPB2dLd2NGejJIja29Xc0WlE6b+G+VbxEsOa96g+GR31Hpii0j+2UWt9iTrvI1KA4E6Na52Mhr179Mn4GEjq2yqY8syUc/XfRA9FW/2rWKJjJDIeztiGtIw9EtUyzlHYV4xnJWH9t6haTX8DICrBJ6fiQsYOPj+YwBR0v2V68Il9x841j6+6XnNdcXEVpADujXMMXhcYvMHjwaXcYtotJt0iTy6Bw+QIMTnCGzweXMotp91y0i3z5I3gMDlCTI7wBo8Hl3L70m5f0u3Ltqqi5ro1Wfs8uOshBm+sZ/Amj7/N4+/weHCpihfSFS9ccTworbgqfXnHlR3XHW8WvVV0jf4flFde7f3y8VePz5dVvrr3tb1X9r7Rdv1Q8qkd4G4IHJ5j8CaPB5eq2Zmu2Zms2Xnn8N1QsmUU3L1mBu8fPMQDR46yALjUrrH0rrHkrrH7keh9PQbC6pS1z8bB/YuXCiJmZvMjfmyxtNhabfmRHHyCat7DKAYjeMgAZDhiO47vjthO4jsEDxmYr1oF2K5rBgfYZvAQgzd5/B0ef4fHg0tV7UlX7bnS8qCi6urwlxNXEtfFN+W35GtyNmLjm5vf2nxtM0b0fvnSlUvXa99c9daqa/A/X7ny9VVfXXV11fVaGLAvdIKDAWOwmcHbPB5canVXenVXcnXXPe2DM8ljA9+f+GDi/Yn7JwZTJ0LpE6HkidB8hedqy5cvXrl43f6m8y3nNfovqKQLHFZCsJnB2zweXGp1d3p1d3J19734B4nkwPHvz34w+/7s/ZOnUyeH0ieHkob7ASOQK8eN3tyovbk+ueUgONg0MdjM4B0eDy61/lB6/aHk+kP3e46kevrTPf1Jw82XV7169LWjV46+cRiIeM0+cDeaGYTmMsjjwaVqO9K1HcnajnubPng2efjI9+s/qH+//n7/8VT/yXT/yaThFpsFUPNF+5V0+c9zv1LwvnAHUrTMHsK9jHxX2J5C+a6gPddX/4zkzuXwULoID8vuQIotufsOkCrK8382a85lWeIvvw9z7uXTzFqjZzfmafM2WfRTy2Dm86OQpfYxS0sIFYt/8mxmCc1c9mfOfk407vkpd0Nl1xdrKn9+rav6CVr385kzhbLl8nPGNoq2gMeMenGeVPk5trXmSdta0HJHtBi1z1rtrCP7M3i/MB6d/35lwftVhbuPn5Inr3oi+sqx4Mw48nO2Wk4mZp0z9rkVliX+PsfRXr1M/qeWm1PLUkvNjFOrRVtHoqiQVhadUn4p1yqjrfn20/kpFMts0WMpaX32Xa6FpPDMdQHFunIpUFu7DEbWLUMDT6YP+vxo/wuLRmJTXrtKZ1yFP1b5OdbuXZQ/r3Zt/SJpKP/9hmXK33i95knwOmOFGXR11j3jnsvRS2X/tIKZegKwMls8WzJjny2dsWmbuNZjY3xrNs9c7eJyAG/PZcMzxTMlM6W/Cz35A7M3QNVtUOLmJyixYdkSo59Lu14vtmj0v+hHTEs3WgRLzHHBxrg3yiLWAnrRnikYsS3X7T/DtX/rT6XFXa70bcuveY/iLXFfNvw4LrOktffz68Gzj8fPZxqtz29V2b5Ea6RsijOmPlV7bslDWfVMH0ZKKNKILRR72y6GJqbGw9xKbPM2ZorYKb4Fa2PC3de1vyF+Me7N2Nv6WhKl3vYIJO0OTUD6b1pQaaQnVrPI8cnhEKmoopNx78jkdFTz6jewSLe3Kxwfm9S8GVufAB9R/wZGr+Rm5oOhWOzCpK55OyMTkbhX/5cWUqyNRPRYfDwUi3sXrDOJYva8e7c3UZ7N0T3pXbBtjn28DrK8Y82UToQuDsKLs2E9lvAUHv9JlFEzW8Yno5HoaKLC2zcZD42ztndo3oUV3o4RLLEnHJsehw7bDkQz9gMjIwsV3uaIPjUeioa9XZNamKn+9P8BsWctp3M9C2uMYr37QrGhcDjqbZlEpKL6bqHc23egr7nTe2C/t6PVu6CYaZuHhwFN8Zi3N3QeEkai3pzzk4NdwiAqKwcP0AAs1HkP6uFYLGub3zvp3RMaPgvl818ZxKGaurRtzXK6QDwpl3HgLxtmSmJT45E4HimMZSoRE92T8XYcujZdn9RzTeWRaDzj1EPR0XCmKDQFJWgZR1wPa/pr9Ho8HNWvY8hJJTKFYlFsegiGNOMITUUE8sWMffJsjAz3ZGzfVqb/Hqa0jUxmnBNAJRqee47E4hn3VGxwHAkiY41k7F09XRlbfDzjwPMS0BgtlnFGgQhjkA6IAXPE8FRH7ngzneXvGR4OWizk4l88+tLeV/Ze3vuVtjcOJatGwV0XODzH4A0ef7uSQ/58Zz2Dd3n6uzz9/Z5eHug/xgOnBnlAC7NAqmwsXTaWLEONXioylY5MJSNT86WeN5qTlU3grq/nMMTgDR5/m8ff5vHgUqU70qU7Lrc+tNmdJ6zz5ZVXN12NvXrqtVMflXs/LPemyjekyzd8VF7/YXl9qrwxXd54xXbF9ul86dMPLVbIkOubqtI3nNcrkyvbwAESCN4QGLzJ48GlPO1pT3vS0343/r1Esqf3u7Pfm31vNnn4GLjU4ePpw8eThntox+I//fTTH+ajuw0copvgOQZv8PjbVg5DDN7h6e5WMgguVdaeLmtPlrXfnb5/8NBDi6Xb2mzj4P6RowURA8cLIk6HCiLOjhdEnNMLIs5fKIggXWtOBAefWCz7rHtQdYrgIQOkh92H71psL+I7BA8ZmC+peENIelRwgHoGDzF4g8ff5vG3eTy4VElTuqTpctuDkrLLbSYpIyXUzFevfGP6RmVyXQ+4G+cYvCkweJvH31vPYYhBcKlVfelVfanqw+nqw1fcV9x48MFZ86CqGh/g8dNPzXog8JVDyZLT4KDtDJ5j8DqPB3JhkD/f4enu8HT3+PP9Qz08cLSfB06eYoGUI5R2hJJ4tn40NRRJD0WSQ5H58qqrwVcHXxtEwtWszL9ifeAu/42yL5cx3ehxcKgbRYi6UYI8/g6Hd/n7e5UcnmPwfm8fD0B7KIAOmjR4OnXydGpNKFU7lK4dSrmH0+7hJLn54vJrG5LFa1PFa9PFax9aVjjlueqs8aHc80b11R5UMeOJnys2eJNc8QIaLF5AeI5BIHaCd5oZTLl3p927k+7dd2u/u+p7q95bxY0fTeDQ+IEQjR8Ib/D42/z5Nn//rphyP592P590P89zD4LD3AgxN8IbPB44DME7Vg4PMXiXv7/L893j8eBS7tNp9+mk+/T90EgqNJYOjSVDYw9qVj60uItl8q60Pqh7+ndKfrtkTnqz4q2KVzuutFx1Plj19JV9Dypqrsa+/NKVl+Y91V8r+c2S6/Kcfa7t7a0pj5T2SElyDypXXqv+zTVX1zwmzQ8f/ephJTajHMaDBoW8T9D7kSUvbikPyH2p6B97Lc6SZEnrV4CMW5lLOdrSjrako43Pih3gcFYQPMfgdR4PLuXYmXbsTDp28uQKOExO8ByD13n8TQ5h1hLE4PCdjXeG/2zrd7b+0cSfTqRKWlKO1rSjNelo5eUdBoflETzH4HUeDy7lOJJ2HEk6jkDyx/cjCA4LIniOwes8HlzKoaYdatKhzjuKXum4MplyrEs71iUNF0PR48+r5Va35Xvu5s1tPvvdRiv439/VXLa/xPKXJY79HvtfB9q3HNlu/9vtjiONrr8VreDn2SJQkiVbxIMStEWMWmZ/cfaIghNQBe9dhWeYlnlfaJ8ofF9yve5npE0ttDA8qc6pfPHJl+JfllFZsQxWC08zFb4v1IEXvq98wlHJscv8IkeoUPsdrdpoiefoPjdZdCfsDatmbXlWkZyzSTO2RRrUllm7Vj2X0/vsn1bzSt7Z88IzG62PP6XvmLHMlSxVbqEe12p5rTX3TLe28turFuk0nY+lzVwtf67G+LHahtmivN3/cnrtQi3wL4tOs1D77Iw/ndeu0pmin6FOc82ytVt/hrU/vSh/Xu2L9NTrCt4X6oMXaWyfUKOKM+oPZ10z1hkXfbPBPWqZcWswc37NliXR160Ut36JuA2L4jZqlkVxm5aI27xE3DOL4163alvgsxU+2+DzLHy2w+c5+NTDpwE+jfDxwUeAjwgfCT4yfBT4+OETgE8QPip8muCzAz474bMLPs/D5wX47IZPM3z2wKcFPq3waYNPO3z2vm6dLZ5xzuWcrcz+xb3Z8Ix7pvh3gVb+wKQX4BS3fip97L6C8e74mepjX/yZ6mP3L79+PIovxjdkw79AfWznMvrYzzJan58+tmuJ1uR+O8i0kWjdS+pjDxTqY/U/RI80sU6vTwh49f/RCKv0VUIh6E04APj1OUyJmlRSxC4UefECVy9AhaDLS78O4l1wevEGs4+vQFv0/8ZScMsPdg/F9X/Eqwr2Q7PwCqaTG2atS38nOBcdOV+8y+vaEcvXYCK9thE7qIsQ8Y4jU6SHotrkRKZoeGwyMhzGm5F0vOSoSIuMRuKxd2wZW4MvYx3MPW64ULxzNBwNX5zSn0/UDmkNO1HBPB57vsGM/i42HJP+B/i/bEluPgzuvXM3Rr41cbv9T7tSz+xJP7OHxeY6Ovj0MR570fHSKf3PsLLyfF1x7Z5W42Do4Q7ziOdCCVcao764xNsbmfC2kEb4f8ZyvoPeH6F3B73/BWvBAzgfI818jN8V+hhR9jHikGnGSyLe8cnzYe+lyemMO4JBDBWFxkMTkWimKBoaioyHMkVjofHIBMAzoWg0FIf3euRSiN5rEMgUAS5jY6FE0e7duzdu3JhxjYxgUTpgmSeIhYaGInrGFQtFz0S0EASmJ0L4pmQoFB0dD2nh2FimaITKzRThJV+KArnGQmPUjOmYjtWeCceoWaFLkJxKjYxMjxPUEEZDiQmE+EMDeMGOIAqiJGeKFJ/fF4DngA/vJMwUiT7JJ/swn07lTYTGoJ1QbgiaOaT/a0QPchH9PfRwkPX/Fb0/R+974G2rebyKW/8+eJmSI6Hx6TBTZP9bjP3v0PtL9D5ADxXX+j30UHGt/zXmseuaoH+Ij5ctXEX9TomewVeOYRhp/Po9abSjE0N6xh6dmNIfYML/jTJPxS7qf4eP8+DFSiy5+mimjX7b8HBWx06QNvpB7aqrjnlP7euur7quuiCAalgNHKphEaIaFuFNHn/7EIN3+PNdA/L4exyifo0Fjg3wwMlTLAAu5QmnPeGkJ3x/5GxqZCI9MpEcmZhf9fQNa3JtO7gbIQZvrmfwNo+/w+Pv8nhwqVV706v2XnU8tDkqN8/XrX3T9ZbrmuuGExr8zCVwN88xeFtg8A6PhwYTvMefUYnOAkeO8sDgaR4Y1nhgIsoD53QWAJfyJtLeRNKb+DGeSSBN7Iy1BbWtCB4yMO/deKPt5qHks73goCkMnmPwDo+/x+Pv8XhwqU196U19Ke/htPcwHhr9dH7V+ocWa+XmrPfAu4kdKH1ohydUeT+9fm7zm51vdT602Cq3kXe19cE67++M/vYoY0L32pI9vd/f98E+CKc2H06Dv+5wet3ha3bUmpX+dulcS6pua7pua5LcfO3quaFk7bZU7bZ0LRRYUrnr7V4T1fNrvTeq5/q+sfpbq9889dapazZ4k1x3+GYIPHC3mxm8xyHimQKpuiPpuiPJuiP3j55IHT2VPnoqefQU5EUVchs4VCEjRBUywts8HmiAINAAwfeGUnUd6bqOZF3HT5JbS9XtT9ftT9bt57knwWFuhJgb4W0ej7kQ3rNyeIhBpHYWONrPA0DtFACXqptK100l66bunzufOncxfe5i8tzFBxu3PLTYV+8i71rLg2eefVv6xtic/aHN8txg0dstt2y3Km/Zvr0XCAieb7W8a3u38l3bn/Lnd1ves71X+Z7tO/z5vZb3re/b3rd9jz+/35I8eCh5sAfcBzwq2Xc02X8s2T8ALt13nEeeGEyeDiVPD4FLnxjmkdooD4zFeWD6iywAfrOtw2Y+vGjryT702o5nH07YtOxD2DaRfYjazmcfLti+mH3Ybd9nNx867D3Zh1778ezDCbuWfQjbo9mHSfvF7MMle5vDfGh3dGcfDjiOZh/6HaezDyFHJPtwxqFnH2KOl7IPM45Wp/nQ5uzKPnQ7j2QfjjoHsw+nnWPZh4jzXPZBdyayDy85W4rMh9aizuxDV9Hh7MORolP8Yc79wLvx90q+WXJTejt2K5jy7kx7dybJPXQhgVXAfKVJS94n6P3Ikhe3lEeK6MXRP15pqVyZXHnwOqwLB5lLeQ6lPYeSnkN8+dgLDpcPhLh8ILzJ48GlPPvSnn1Jzz6evBkcJkeIyRHe5PF3DHiIQXB3N94dvrfxu2PfG/tu/ffqUysPpDwH056DSc9BXl4IHJaHEMtDeJPHg0t5htKeoaRnCJI/vh+t4LAghFgQwps8HlzK05b2tCU9bfOeqq8WX2tMeZ5Ne55NGi72DKyyf76iZVX7M5a/eKasXbH/hWwF//01+5wH6+3JesdBwZWUreAvrXt2/0r3/Cvd8690z5Zf6Z5/pXvOafGvdM8/ae2/jLrnvbm65xmXtj5fAzxjvkVYqG+m24k2apu0zaOu2eL4umxdcx7LEn+5WsQldbX7fnV2lj8vd3b2cbranDPgvzo7y5+XOju7JZvijHn31Gc9O5ujq3V7t6v4C09cXcseRZ+XhQKi4k24KBRUC/S2+v+B3g/Q+z/R+3v0/sHyi9LV6j9E7/8GL++b3/8P9mplJLqUFpYa+/9ajKsc8Sb5rF41UZanVq1jX49frFnVP8Ec/xm9R+lSSWWq/xcLXrSkBMQA/jQOhFSfpLJQgP6FpRSIn+nQbVdPV8Gh2xyVY+1nUDnqqwCxn0XXSN+hR4WjXoc58hWO+mrrI7SH7xge6hxj/c5Hag+nwOG2CSFumxDe5PGoPUR4hz/fbWbwnpVBPAXHAkf7eWBomAdGRlkAXMpzLu05l/Scu69fSOmX0vqlpH7pV+rD/x+pD49CZ9cdBQedJYgHRhHe7zvMAqm6/nRdf7Ku//6xU6ljp9PHTiePnf6vV324edvbG7/RP2d/8FzjLestG2oOb7W863i398/c79W8N/z+hveF9zd8b/S7T79/JnlsOKlFk9sn59zzv9Ic/XPSHLWvPeC0/7XTcaDY9ddlVvCX1hyJlT/pxcqLdl453+GP53xXnySekrxne8F7R8F7Z8H7ooL3roL37oL3xcu8L1nmfekSeozH3JuWe5PWT9nzsmV6vli79MsyJiuWwWnFMu89y7xfSrf08xmTqiceE+svyZhUL1N+zePLv179M8J47TL9WvnEGLf9kmB81TJUXLfM+9XLvH/qyWZBcf79yr/AESq85Zp0rPn3tKCOdc2sPU/H+vMZ1aeXuL95rbZu1DbryL2/ZcZeqKe9aj05Mutc+s7mQm3sbJG2dqboPOyxtC/M5YxZ9k/zvpJ3X4y2/on0wq7ce/K0DdrGgjt2ljyTOPMI/Vd+TTPWz5KKdG9MA0c/zKK5Kcx0b+VMM0fhTUvpc6L/8pF42VyAl2f+a8JLQeu3FLQ+Z34/qv65quXTzLqvWl8by9UzaVu/vW2RtaA4vi2bIr49G55xP3a+l3zWmaw9u8xc3r7MmrVYd/a4Nevz4yHPLc8RZ0qWHN/Prw31n6ENliy9MWr8GbanYVH+5/KeGwve+wreC8uULy5hRXjMaM+4Wy0n/3a2dKZ0LodjZ/+0AtqhO0HKZstnyufqlkxfnp9ek7Jq7tkVxZbPnE/OyVdBK6OYTc1XRmW2IndlnFnxWTjPrGem4jOlq5zxzFQSTXg4RzKe/BwGOAwyCCGVxzRxuIPDnRzuQjhaOls1Uzz3lGWJv7g/G54pm6laZGP56IltLLmc5PkC6nlhCa3950fru5fgPJ9f6c3Lz+xHceZ4MBt+YhvL59eDPY/Hz2carc9vT9eyRGuW1oG0LmljaetOrNAnvPX6iLdhdIJU8I+0ubi8PaGzkSFucnF5e+kp4fY20/Fob6LI2zM5EYomyrzteHdIzq0l8OrsGCZxeTti46EJPFkfGo9gluaxibCWKPV2howckH833ZeLP9Dh1f8YGzBnMWw4jzLfQDs6Q5NaJDqqf8uC96TIv3wGnTrWrcUmnSoo7x/xt4f5wfqGU+gOHrp5/tuzd45852SqcX+6cT+PznHMAvRfaDz4+GWsIX3zP5uO16I5ZqvVsGX9E3p/Ysk1aOHlEJZE+V4swLApkfEqUeXtC+mj4bi3fXp8nBPbI21ZaCinm24yTqK4jF0QpYwTD8wrGQeeoAcfT8/bA0F/xiaICdvu3QnHbvhb8oD8JmveAfm1OeakJ7Jb/V/o/XuLYcG6i95Waub45IWwrv8FRvwbyyPsWn+FKYt0ugImU9IR1cIX2fn7fFvXtuqMk67zyTjwgp9MkTaJv3Ojr7GyH7jDX2+xXdQyrnH+dREHXVf9N1jIA2pMHL+FQefy2YH7/x1jS6jMQbwXJlOMBbOgbQRKG4+xQ/nVlvxLYvLsa79veAuY9J+K6a4Y1A8nn3o25dme9mxPerYX2tomwKGiGSEqmhHe5PFoa0N4hz/f5e/v8vR0Qp8Ch4/wwOkQD2hhFgCX8kTTnmjSE70/GU9Nnk9Pnk9Onue2jn3g0NaBEG0dCG/z+LtWDpsZBMcMLVedhb2IgMNeIMReILzJ47EXCO/w57vrOQwxiNdXs0DfYR44cZIHTvM04FKeM2nPmaTnzP2zU6mzevqsnjyr/3QWw8JeQK0nsRcIsRcIb/J47AXCO/wZ7Z0EQwxS4ykwcJwFUp5Tac+ppOfU/UEtNTiSHhxJDo7Mr16HV0XvA4dXRRNsZvA2j7/L4+/yeHCp1R3p1R1Xiz5PtN/j+chgSwH8dgcFQkOPxzqztK5bf2MzkMzWQ+CAZBg8xOAdHn+Px9/j8eBSG3rSG3pS63rT63rJoPnDz2DQLOi3DA77jRD7jfAmjweX8ihpj5L0KA9WP32t91ox0OtTX5hzvvncW889tLgr262fkH91z/yGrd+qv+VMbfCnN/ivuR6sWTe35drz155/sGXb71345gW2Kt0/PJA8fiJ1+GT68El4TDWcSoO/5VR6y6k5x7x309yxt2Mpr5T2Sh951Q+96rub//X2/2n7n9V/p/59x1+X/NuS75d9UJZq6sMbjpqOJQdOp5pOJ0NaqklLhs+kms4kz0ZTTdHkZCzVFEvGL6aaLqa8l9LeS0lyP/jlaMn82vVz297uTa0V0muFj9b6P1zrT60NptcGP1rb8uHaltTatvTatmu2N22FlmIPWYq9G2+0vG37xt5v7f1G2bfKrjmzpmO0FHfhF026wOEXTRDe5RCvGkKYqutO13Un67rvTX//wgcX3r/AmVc7OGReCJF5IbzN49HMixANtu3MvTedWteZqutK13Ul67ruhe8f7YfV+LC1zcYBzICCiNBQQcToWEEEXeaUE/Fj/HrFHlt+ZBa02/bj+YDD1v341Gk7yJ4O4tMh21H2ROCAtR+PECB4yAAUfcx2CsGQbRgjB21Tdg4gcswWWRw5zr62kR+p22KLI1vsrfZFkR32FxdHdtsPLI7ssfcujuy3H1sceco+WBDJwSfYv3P2HzHwkAFsrv0CvtPtl/AdgocMPNj0zENLKVrQwbvW+uA53x+++Psv3oq9c+DbB75RjLf6PKgX//DE7594d2Oq/vl0/fPvnkvXN8+VAP9av/MHsvqvOv+4873qlNyWltveC6XlfW8Xv1386fwWAbjQ+p1Z74G8A9+8XQz8aP1O4Ec/2Nz40Wblw81KanMgvTkwZ3uwueH3Br85mNrsT2/2w+NzDW/r77Td2nCr94+eebfqj7a9u+fd6T/b917P+67vDuB3enqPpQ7CDDyRPDmYPD2SOjmSHI0kz0ymRieTU3oydiE1dSF5MZF86Yupi1+kL+zQOZJW24tIGc3sCrDn9tse98WRVYiYUg+a7g3vE/R+ZMmLW8oj8//i6B9v+JX5/7OZ//eDAPiXDc1lnTssH+wo6yqx3yu2gp+ubV958il75rk1x92Ov3NZIfx37rLjq1x/V2PD8Eorhlc1++Fh/inHyXWu+fVW8IdzfijagrttOiPwH8rwjEDxI08JaDbNrjk0p1akuUYLfqd01rb0pmjp33nV3HPOpeJHLVrx69Z4WTbm65bXrVoJxK0oiCtdIl0ZxHkK4so/Y3krPufyKn4O7fO8XnByI9fSlmtJia/MhvNzjNgW39ZtfcQGdy6n/pzyLAXaV2ur5arzpHXWrlXOOrSqvHPAuZRl9lCr1mryNX+LNVbsZvFHlmVqjLSV2qrlyvqcWlT3GctarT21bFlr6LS7M2LRnp5x/pYVrZLgf0Hzgr9e2wD+Rm0T+Js/Q33PFNqO8uuDUrZ+LqVs054Ff7v2HPj1WgP4jZoPfEETwZc0GXxF84Mf0ILgq1oT+DvI36ntilhvWGeLIqgRzG3N+pzWPOK3bBe15AVtN/jNP3U5e2bQb5mxg9+qtYHfrrnB36vtA7+DYl78qWvZr7WA36l1gd+tHQD/oHYI/B4qv5f8Pu0w+Ee0o1q/dmzGoQ285QRsuR5xl8fxGddM0bdP5OvV53J+uzj7V2gN1E7OuM/jb0D25X3vx62dytoqCjh9sTa4NPfWTr+COUPZnMtYbEty9ddnTB4Vb8yJNS0r2tDjtNpzOd88eFRvl7ZOaMOau8DWunQ6TQt/pnQjhb96M1uqjc6Uft2iDc6UfN1y3TFbljeOJt61sZlieF/4y+bmN27QQqVF+P3yfxXfkVNncf7aoJXkrx9aacH7soL3Z64XzxQTJzpTkPLsopROsvvYl7QjPEmbxhe1KW9t1CYKa54pA+yULaoz5xb9M+b3fZam0PjzOe2LFozSip+4pMmCkirizdm3Myu0qfz3imXWk5eiYokUlTOepWWnmWLtXHYENH2pcZip/Ex5YxQue3Q5uXLD3HrLEn8zxYvtJk9iyXuy1PDmvnYeeMyF7HTXLmbD5y36nxfwsdyUl3LCj+FveVSc4PMiF29FS+LqJ6WelwqopyqPNqqWoI3qmepHju/Z5WjjCS2trdnSPysFQGm2q87X7LnSqDaTKLdYQsXsN+tzvw92xvyNhTNm7CZSzsf356R6xixptrA+9sv28e5sashfOluD8bM1L9fgWxa6YDXs6tte7k641hwXdqjCBA+IRkA2AooR8E/oFy1oRKIn3wSZzpjdA82BiaK+rv31nb3MIvgqev/KgrfIH9j/Y/y+2N9f/xMv5pQCEwv1kuLzBxVFEgJicMYvjgSHw+pIQB4SICgPC6I0PCxKshQIySFJTHiOt+9p7m5s3yM374DQkcaPscCPu7BWZ4MP/j/G71N+LFjwyi1IsudIY2TvjzyWyCc3z1tCMI6WHVsKy/ALlFMMBvwsh1+U1YAs7ChMqKiUUFAaJEFiSUWfTw0IKmZs7Wp8SQtHY5H4pV1Sg++5CxEtPrZL8AV9z42FI6Nj8V2CKvpmIWVnS2M4Orh3DwRbeho7ulu9oYgeD4/Dc1d7Y38kNDkRweJbs+GD3Y3DkxMNI6Hh8NDk5NmGs6F4KBrCWo80dkW8MqbphRZiP3ZEp8fHoejmxpA+EQ4NRerPB0JNPLzj5ELJ4VhYr28eDUfjCxXNw8PhqXh9W3SYrKEL5aOJyNRzXi08Mh6KhzMlLZPRKPtt1YxzeHwyFk6UDU9G45C3Pn5pKpz4QmhqajzCflqi8UxsMrrDOzwW0mPh+K7Dfe31wYxj32QsvlA1qoemxrLth84kyi7WjwzVxyIT9WPRyL8nSr3yN7t54B92L5T117fvqe/t6Krf192RKW+ejo9N6pEEVbUgHcBn7xORz0INlZjtUn0fdCHjONrR3rHg6a/vi4xCXEesvicc1y9lnO2h8Vh4oYI1MxyLYY6ItnA4GtF2nYkMbL/U3b1ndOhCy44piOgKRaI74hAQJBiB4V3CjpHhXb4dQ+gNQ/SyjaukerTw+chwuH5Un5yeyjgUQfQtVFGr2/VIOKqNX6pH02Vm1ZFI+EJY7wmHqCOxruk4w8saStwTPjcdjsXrm6Oh8UvxyHCsvi80GsuU0SjA6GMd2GNIuq+v7yAM/2gkGs44OyOjYX1hBUPTeARHueNgxtGnT4cXqtlwQGagnpbx6VgcktZSo4ezGI1Png1HM96gIMihETkgaD5J9YtBbUgZ9geHoeuB0Igq+TOOkBbRMkUjk/pEKJ5xIOVkilnnB+GFM4w2RfbzEfhbIpnVaAPWgSQHQ0afBofHQ5GJGP3eRwaocmJiOgqTD7Pbh6fG8QcwpsMZFwzlYHR6IuMZCU1Exi8NZivxDOthmLHxCIzzIFJzpig2Oa0P4z1ik4CQTGUYzaOQIw6NYSlqhqbj8cno4IVIfGxQi8RCQ+NhLbMiHNUnx8cHJyACyDLjHEHSydSZjebkMzgMxB8JxzLV5puJ0PAY4B7b89TwtK5De6CRUP9oWBuMRAfxJzUimo6yuz5FbLStN1OGtWDLh3GSepejrXecmSIypocz1cM0rIP0LUvADF2bVjcyNBiaigzq4XODI5zOmHXWhdFnw5egRmAUMUATjm9i81g8PhVramxcPK0bsWmNhL93bBmHBowq4xoLh7SwHsuUGnjAIu3TMJmsO5Y+eoAigXn0oI5+w92SI6+wk3xWreC77vyYwWrN3ov3GjqwDwvWXRnnebxsrlufgTTv2PT/iMj8yLLkt2h1TVji5MEL0Ei6OJ0fuajtBndLuBq6VvTVyJz99Ym55rnRb72YWtnAXuU6OqyQqSgggY9RHNBft+LP1GzX/5OFH0KAxbO5q6NrV2KbgWI9dOZiA/sNmVD00oWxsB4mPI9HzodfABTuyjg6O460sa8r42GbTFHLgQP7O9oWbPXPJypxLWZf6K1n35pN1OZEsZR0kmcbNsXunfHSgZBEsXemHv+e90L5B1r2J54qL6dV2z9xfNfJl49TM+vxzUnvgufChQt5VAATGKdOxjUBvQ6NwkLCpxKQQ2INliQFdyg7ZP/E1l3bXt7KCjuwf5t3obTzQG9vfctBahMewfgYd+7btuacfUDhR8czu3T2gR2FyB6eoN+5cYxPTk6xow/09V08JcZ+C8eFd13iz+UUY4B+Mkf/7/GFcxqQKeu/QdmnYNHSz+KBh6KhUCzslzPFQ345jKtkmA5vZFzTxqWZWpgmkUsPT40DCvSrNLAW41gH/rRfpnRkchxyDk6F4mPs2AZ++xj5VAxQcxHXYGTjmYrs4lT4Gz/FbUaybbXZewwztuHxjB3YJJuhYT5D9WnqBs47/VXshm1qUn/NShclnj17NuOIxYaGMkWMFjN2HVhSGf4IOTVwcPJspjL7ZPAsF0XBO5bSiC42U7IfC7KGY7WWJY9xGBONTpqgJ+KsKirBgxwPbc/ZXD90lb8ye3VirvPW0++Ov78z2a8lw+eStXrKFUu7Ypc3zNucrzz7ka3qQ1tVsvrCR9UXPqy+kDTcdWsy9ymU+3TjXO7TzUO5T7cr857yUt5pzn26uz7vKa+Ge3kp8eRI7uPR/rzH4yfyHkNDeY8jo7mPqeoLaYi8NPtji+WLxi/WtKOd6ovWvWjBRIB3uVnpZ2xqyLd34Bs7XUMH/o/xGroujHrR1mf7JwQDtv/MwCcITrB3J2wPGXhQXvvQstG+4hP0Lg8/qN5zufNBydPXe2+s/Na6W7ZbYmq9P73en1obSK8NpEoC77pSJS/ctd9tT7f2JQ8fSR49lmodSLcOpHYfT+8+nio5fv/E4P3TI+nT0eTkuaQeT52eTp+eTp04nz5xPlVynppPX+wubcbG7rGRobfd1ontarfRT6MfZs07adMwYbstzN6F8WmPbQSfEGAhI5hw1HamCB/OFF3e89BmKRspvdJ5bQO8gFBybcPbX2TBd2fe38sj+9AarTFDMjw/ZC3Ae+VsoWzckG0KG3fOFkcwbXsJa562taDVtNW+F8E++360qE7bOu0/YuATzNCFTwjMsrrtJ9ACe9J+GkHIPoopQvZJTDFljyGYtl/E3CFmnUXwCWZI4BMCs6yX7C/i9Xv7HbudZlyz8yg+9DtPZeMG2cV6uvNSNi7h3I935XUWDbvMOM11AR8uul7Oxn3R1esG0OeecJtxUff+YsxbPFBsxh0vnsCHaPF0Nu58cXsJgL0lXSXZ/pcM44NWciYbd7ZkD4KW0nCpGQc+/pqWpayr+Er7G9Ib8a8mXp/56kyqelO6ehO+7yqe6397hIVuHb9bfbfvewPfPfG9E6nmnnRzD4tP9g4kj5/i4cFI8swEC4M/aSWT735bt82MO2A7iQ+nbKezcSEbJ62JbFzUdgEfLgIhmHEztm4c0AP2HgS99qM4Wr32kzh2vfZB9jSITwdg6H/EQLYWNvJx+8vZuC/a9+Lo7nMccJhxBx3D+KA5Etm4lxz7cVg7nb1OM67PGcWHSaeejYs599EVkuz6RBbXVRShSx2LJrJxF4pexofDrmNIBdOuFhz4bvcUgt3FncVmQtO/3DpfXPna2uSq59/rS/YeTRb3p4r708X9HxWf/LD4ZKp4MF08eHnPA1fNNVvS9VTK9dR8WcVV21Xlq8Wvdr/WDcym3PMb/V/uZ7LTu7bkjs50sAuCqdruNPjl3eny7svafHl1unzt9aG3zrxd9Wb0rWiqvD5dXv9RufxhuZwq96fL/R+VP/9h+fPvxt4TU+Xt6fL2j8q7Pyzvfj+W7D2SKj+aLj/6Ufngh+WDydPDSW00VT6WLh+7rD2o2HzNkazYDO5anMHLI/NlNa91Jle/+F4veOBSZfvT6A5CY4vLrhZ9ee2VtfOusmT59jfWgwcO1iKCNyo5PMcguLdbUuWNt8puN98qu1V2x4r+rbJU+c53e1Plu1Ou5rSrOelqpuKCWFwQHBaHEIsjeI7Bm80M3ipiMOVS0y416VLnV9Z9dfRr4785fmNH0teSWtmaXtl6eWZ+zdq3Ar+z87d33ixNKp2pNV3pNV1JV918acXVsmvDqdIN6VLgj3bXqrnRm/Gk3PZejJ0kprj3Zx64Vvz67L+Yvdp7rfb1Y9dir5+ck1O1W1KurWnX1qRr6wNX9Ueu1R+6Vl/beC385ra5ljfr3y5NPSX9f9VdeXAU15mfvma6Z0YSMxrQMSAJBAaB0S2QOAToAh3oltB90YMQ6KJ1AMMIBooty1lSFg6OZQcS2Wtv5JS9q9q1d5WqeIs4dgVv4XK30i5NVKWqZGu9G6f2EFtshc1f+77XMz09h0DEJOtFj99739Gvz5HefN+v35srkeL3zWdL8Yckw2HZcFg0HF42GF9wXnNOJV+9cv2K+8qKAfWPd4LhAcBDXYAuHGAaxRO9vm5vrM5gdjtQZdw4Lcxsv31pNk9OzBE5KMqTu/eWabpCXpcyu01ely6ZM2Rzhvvkst4kmlNnRyRz5lyOZM6dj5bMB+bbJHOppC+T9WWivuxLq+3W9leff/n5O5dmj0vWfbJ1n7sPbgY3nSWZEmVT4oqOMGydyfYYTMrlmjp5c/t08s1d07xk3SIZkmVDsmhIXqGQF3bF8ADgoS5AFw7wCYeqv9RzL5y5dmYq+urQ9SH3kEdvcjt+zUQsk/pJ4up291b4ebTMrpNZu8zuQpuQFj8gr+s7J2uvpl5PdXt/lllsMvjBQ+qVbnBXcBgU0qJ6BAKG12ozmjJ1C1mWBpr5BX1kU/1ug7zZjAR5N12fYZIzKGhnE9DOwe1cM9rgC5puYLkvWAraJgLa5gI9EhatiScOMosZ4LR4kG4iOA8BTh6agDazC9qZO5ozqF9u4gCfZxAGTBsBKSdlwlHmcdNG9AbRDwKnJT2jhpeBOBIYcMavaoT3ZXjmj+Kr5w1r9mV5Ltj3DjdBBLwmE35LI296XNp8ggx/LXt1vPnN4KtJreobEeJLr+obGeLLrOobFeKrX+Xer+MtvUGJygkDb51gV/GPDnlWuFWuoI1f/xT3f8NT3P8Q3zvMhBEds2nV6xETcj3Mq/rGhvhG8HHaJyZ4Mk14zT/AToTY7QF2MsS+0UUh3OSiESa4mO/BhIzaLQwhWyQF2PUh9s0BdlOIfUuAnQ2xJwfYuRD71gB7RIh9W4DdGGJ/7o59IpLf/gSvHU/YS8odJsAjKKmMk2c7ccAtEhNzolxRdbqUXZVLNORGvuKRru8jHMhK9b858xXEZr6C98++gvBKn/u707q+Hx3+HyqFcVIZqekAOU4qE1qZ0MpKTU+hlqi9melLNGRN4A2b3PQURvg5hAvuAXyKAxgZ2dlgzMtExqWISsdwd39nvaPfAWEnYwFeMaO/b/DsEl071NO3ZD4qdA84HIPDp4cGHUv6IzjTIpyCw3TooLuq4eEhZ3SY7Ap+v+greLNWQIN4XQrtjKorr8lIzcxIz8zYk5qenuGMqlUUGRnp6PDTM5FHdcYR8MjNQGeWsccZVY8Vmel56TmwSUq801zr4Af6kiqHRh1JewOk3AApzxmhkTLSnQZF3Otr5PoaeU5WaSAnbyvviNoqdHJKqzwzXW1m+ZvZ6kY56kZ71NZetZXr77LeuU57EknVwlCAJhdrtCeTHSDlBHjvwd7evrObfK3mzIALkFvv1CsZOadeyccJpeh5cEYF5d6cBm/qzcn6Em9OgzfthrcsrFXq4yVKXVCk1NXenosalboO1VtQXVWdlrF/9XyaM7mou3+872xaZip6rJN2VPQNjl3Yn9SwP+nIIC8M9fFJGVlJTnI/vM5YMNbXz6c5yZSkFFoT0PwLwhudTFm3RJ/q6R6EZIXyLHaOOwQIG4O+Z3zJ4D3LJQaf45JeOUOwnhQA+09iTx5wGG81Mg44cGqJ6YG9g8CPL1HFlUU4SDgCNJOwcbolasRxQfgndGw9EKcDPpVbt8xG3oiYGp86LbGJMpvoti3HbLp1eebkbJYUkybHpKHvgOvxggcIP3ju/dS7lrtHpMwSObNEa/lsw/0EWGqhtU0qbZdL27U2X5xoWI0TBVgvXH4I0SIc8zqmMLUryCoI+1wkqsmHSqXdQiQsy6zp2yU3KqdzZ5okc6psTpXYNJlNQwdvstw4KMYdUIpkOiibDrpjlrko+P6aqhSJS5O5NPf6ZeO6G7vF2ENKkYyHZeNh9wZ8PcQNJ5QisU0y24T6xVfp/IxB3LBDYlNkNsVt87CRXoMY87y4YbfEpspsqnIM+dObp2slU5JsShLZalTe3vNW/tzmuRopea+cvFfRffjcT1LvWe4dkfZVyvsqFZ2vW+WIu5Qicd0y142OGHaGLkJMsV6L6FJxJfqHGN22FVLHttGvUFNFN7lb8BUeSQq+HS1uy1ECfVr1hyfvbv1x30/6tDqxuStA7BsMEC9c1orw3oMvrlYDN66UrIUbV6qslKH1a/HFYHrAr4U8CX4tytsZWr+z5CCohsgR8DtLjoIfVEF+LmUtjcNUEcReXGQxxF6gCvI7TlWDqoZqAL/jVCP4QRXk10F1g6qHOgV+HUr8DqogvyFKANWI8qYFrMHxUF2KQ/VT0B3t0Ze/VzhHv1P6bqmoL0flw+j5+h/H/SROkVD5rFCsbvi07H6ZpG8UT7RK+laxrVPSd7qtHtbojsMJp5OaqXz9pPYtEV5Su8boH7fNaInw6j+emKHC6dEoj7xJBL5yfpPgKaQzBunoMH5MGAq3fo39GZ5xf+yf4Pi4EHq6htAXMGGVhii0Jnq63117L8NOlh9KT58xhfPjg0aRvEkzWQfFrX07s2Y7epBLhn1SE3SzbpDyTulBFumm6PZHE4yLCU+p5yNcVPgpkoLotIF01PB9RbqoNflFuehnts91LnpNfpbgye1X8bOiq//Uxzah56MnDH0w/d2m1bb4DsGv5zcgjOFjEcbx8Qjt/Eag4I8m+rcKT/TmE/jEJ5Dkk55JLwGvAPDPIdzO71gDBR8wm8/BVHsWXYk9AUcTlkz+BPK6l8r/tfvZh6n2+1165WUAhPk84afyY03B195LIb9fQ+U/ivAYXwokftx/OUaViM9X8zkuA1+DqfYBE2CdUV+l4WtdnIt9ty6Iaq+hyfr/BVHtjXy9yziumyKEh9rzchn5hlWpqCa+MfxfIv7Eddiyac1Ue3N4Uv1olkar0tn55sdS7TUE29XOdpXPcQu/ts97K9+2Jr92PmhpjokIvsMVgb7hN2KyOD0ROZqn8SeDpouhgqaL6QyyM8ETyt7hXCYcHQieWrYrxFOhyYenCj/NMXWHHFMgbb4neM+uyLA0ec1UU2fU34fhn67RA5rjOxlCbj+ksYa+FBF2ROUy8af814Pv9cdW+NNhr5BmH66o4H0Agd61bk17Ctv7U1KgNaOTmaTw+wylQE8Rgwa+D31Gz2hIXGcDqOr/HfR7QOvZr2k/5vfDE56kggB5IORJCrQ/7ukO9tQ83fxg2Dv4hz5voS9TfJOeBS0dPin8PsPS4ekbv9eOfnkzpsMbvHT4HX7LU9Phh9dIh7dgOrzlssVLh0ctDR3+XGVYTnt9RhCnXSiAyE0hAKbfqdFPIQdClQye2UrYg8OWMGXVEg3sXWEKNigCKAMoB6gAOA5QCaFUc6GXZQ0U5d9v1rKsL+w+f/78bmDO7h4T+hVOGi9UwabVeFNM1K10jAJvWqgBfS1AHUA9QANAI8AJgCaAZoAWgFaANoB2gA6AToAugG4ACAgJQNwUeAAHwCmAXoCrAH0A8HUE0+iEfoABgEGAIQAg7grD0DoHIACMAEBWQRgDGAc4D3AB4CKAE+ASgAtgAuAygMqRFa6A6Aa4Bldku49L2bP7sYRVYRI2+XMcjQP4NrHazFhfn54qvITPAI72O0Q4JmpM93BfOCrqC0QgFTW5DZW7lpkjM6feKp09+cbxuc1zR9/fKW09oJi0RZk36xbs+RXCSz8VvgvgJ6BSIz0Hlce9qhzzSYVpcHiNgEm0QA0rsOw+nuGjk27zLdCCbGmB9mB6qfA6dGL0Mkt35ytUU+E2mO4AfB/gB+Bk8NJAlTdNAvbr5Ya+QWBa6JPJoMKb0GsQFxTmwhLg94QAJEQc5VSmy8JRWRyQhbSF8Da0gBMq/KX6LP8QYBY/YmB4B1o/AlD5nsK7IPp5nkSz8B5o/grgrwFUXqcwB+dh9U+U5aV1nhpcIvvR/+Hzwt/ABn8L8D4A8DmFD9SH9O8A/h5gHuAf8BHiX17woFh14aiYymMm+gA+ZSMeTuFhpjARX7KmG8ZFNnaBjRXjJhbjJhbiJkRfudMtaqS3j2il92q00gcZAdI5rfRhgOcnm7XSZ0SAFLAHWEVGK55oChDbOwLE7p4Asfd0gNg/oBWluAk5DliWh8kiYPYVk8dIb6jyAUiYPwkVsLGISlDGY+SqwIJwBSPappqsA1U12QJky2qyC8iWUD2Aqkex9YA/VJ4I60ut32qdjpYiNskRm6a75YikSXKFpDibx7LhVfvL9uk6ybJZtmyeQbB1smCy4NEKSYA1GgQkPnrkscav6DZycQ8AJgs8VturO1/eOX1ipvaHTW82vdHyVotkTZet6YvW3AVr7nzMXatkLZKtRYvWigVrxb1Gsb5xsb5tob5Nqu+Q6zska6ds7Vy09i5Ye8XTwNqUrIJsFRatzgWrExhuBJ6Ep5DEfNNozDdFiE43ugbOFiEy15J4dh2YVud3UPFgalYYnM0KZ7NZ4WxG9+IeesnJQo+9bLJihdTZRkxTFW9Hv7H+rfWoDySJ23PnE5XmvY1iY7tX29EPLDwC7xDJ2t0O+HWDpAtuzQR5GCh5R6ijEII9oky1U61MrtNANUF49gjVrNiaQZogW0CCSu2rleqDTs5QA1ANUqPgMUi5wGOCOgyR3AK6mH4AyhL6oVI9gA2OgnRG4fIpfR1TVlpuovESyYqukuFBcDBn/bp+5jIIV5gSvao7qm8CoVk/bFB15wxFwM0rZstZVVfBdoHQzTr9uktsE0T7m7leTtWd5pyYQ8gVGFVdobEOhHpji1/XahwG4ZzxvF93wVgFVbVJMKk6hJNA27Q1cFMld7LujN52vua67ZLsz8v258HewM02zZ1SWvOtn0V/Vn+/5dO2+21SaYtc2qLoxdYe8aTXR+w9JwpjShvIiQTOGNSRjaSqO0E6QDhFnvbr+nzpgTG/btyXCsDEXUVXRDXCDT1BtUDVqhA1WykHPAetSnAfqgfgchokqPx7oS6B4EL3WtUdVfia1cpNVnRN9FkQ+ukCRtUVKnzNeqbVr2tjxkE4r6x9reguMdVwx2v09XpV16A/h9fI1o/5dVf0JfBItBu6oZow4Iehkb0A1TGunlMdVZwsWrbE3dokJh67x4utnaKlS7J0yZauRYtjweKQLL2ypRf9XonaOEOKUVukqC3L8Zume2bW3+57LfV26hT61Cb8IPf1XO9wpEdEd7CkFTWl5DYZob1NtrdNFS3bN8v2Xe8VvFs2J7xT+W6lZN8v2/cv2gsW7AWSvUi2Fy3aKxbsFffqxJo6yV4v2+sX7W0L9jaxHc+lZnfIdseifWDBPiAOwrMg2cdl+/hUkWdT+ky2uCkdldmtSj1VsmyLE+Nz75xDgMrbNUr9XrdSf3BEqVGZj5biD8y3fWKZb0NYAzjfJsWX3kuW4o9LtkrZVinaKnF3xdBdMSrQHdTQHdTQHdQfWpR6vlGpJVuJbCsRbSXLSVveMvzQ/Kb5vVZxX6WUVCUnVU2VLtvQ39jDd6MlW7FsK160lS/Yyu/h/E6p2Nj86XGx5ZRUcUrsHZAq0CkLUoUg2UZk24hoG1mO2zTdNxstxe2W43av6Ij1e+dssL6Y8XXjTNbM2Bt5s3VvHJyzSck5UuweOXaPGLtnhUJe2BXDA4CHugBdOFC4giHqL20xr5a9XDY9crPqVtVUlccWd7PYY0meEWa3v3VpLk/eflC0QFEelZjbZ2eflxP2zjNyQr4Uf0iOPzRViK9pHlzTPFTgmkL9nlf+wCujMo9uxcH5/k82z/cj7Aac75fiy+5lSfGV91xSfKtka5NtbaKtbZUL/c27WlPFv14Xu8yaJ7tfNEzS8PNo2RQtmxJkUyrahInxA/K6YZzKfDHyRuSk92fZZANThB88qCva9+NlVjIRwKyEbx/XihKbo3Qfb7EX5es+PkhAOx/9laI+ISu3I+EXKYn1NkZmzagt2+j6WE6OpaBtJ6C9sTAaCYtpiU3xjCcSnDzxdFMC50kAJ89mAtpbdqH2L6N2tERSv9zHIVziGIQBuUh4QRvnIn/L/iG5yIBlQ9E3LO0CutrYXxDLieCpO8waM2eaPWj604Vkzgzh/PigBVB4JiRztrbt9GvKnFHtf4YzZ2zYPg0uKvxi3I/NYoXviw3JnIX341z0M9unMSRzFt4vZFnoVfzM6Oo/9bFN6PkInDmL1E4iFpI5i+LXIbTwVoTRvM2fS9MulKNdEviMmsPjY/m4J+S84p9JL95c3mrTaa2aSwNM5dPUzFl6wNFo8on+qceekIvy5uS+dj/ZOHOWgzNne/i9CHP5PMio4VzXAaw5+LX3ks/naLJxBTiXVoSwGPdfgtE3LVYZX86nuQx8hTdztlmzP3+W8zjOnFUGZc7WsmSNka+CzJnwvvasXEa++jFxce0CNzXeqHbtYzIy2gis+syHz+tpJ3rh64I+OebRDM0xmvn6kGg1LDOyWrS6QROtbnwG0WrNX4fwE2SFjVZ/wZ8IzC3yzUFT7ATeB61ni6a91vvTGnp/+LZnepfav9F3Kdvf+1PcJXKKuvGCdmzA63FOgfLmFJL8Fv8UY/7JxLw5Bc1UR/5Ji/iOVXIKmmmLcE4hEucUIi9HenMKqKXJKXRWOuO8r9Dv1b5CfzwDNZ0mBFXlrsJqEIyu9HavY7i8gvDPAJBVEL4E+BeAJ+cUhH8F+A2AmiwQvgL4f5EjwAmZP26iQPgtQGASwLnJe9MylZuGb5dvvoL2JCWkbcGKgLXJcbwbh89XjXEn4Z4HcO85mt69oW/UOQS/hRnYAEe7k4Kj3c86so0D2G4AHMXGwfTAUPYT4thRQXFs4d/B6T8A/hPg8aHsoNg1/HUOG7iWfABnM5JmUALXW0nDl5oJAkjrF9X1Ii5fNDR90eyb2F0p0R0S2SmTnSLZ+UXXSbnrzGLX8ELXsNQlyF2C2CV4DOYXLl27NJUlGWJkQ8w0IRvi3VtWSIoyediIl0zfMk0VSmyszMZOW2TW7s50Z0JQFqxGEJD46JHHjL6hxVARDwDcPR7O9FL8t+Knjk4X/ODY68deK7tdJnHbZW77Ipe2wKXNGeZJidsvc/sXucIFrvBuyb3Mz3P/MffTfff3SVyjzDUuch0LXIfY6RBPnZa4PpnrW+TOLXDnROGCePGyxF2RuSu/0+mMxyDMinAFwtdVSpy5QQlFtyqh6FYlFN2uhKLbQTJ2gIDQneWxHnEfWCF1pjOmyQN3qNeY2xCBQpKYkDYXpTTvmu+d8CobTkKwksD7Q7J2r7xf5yBHIAA7Sp6H6gJ5GXZ3gSyBmNlRZR70CqoKgmsXyGrqoVI9gA1qQIJK7avW98I8D5WDOgseDt9r0+ehuki5YGsHNaHYJpS36C8rb9Ff9vd1haqEcFwVXcSoumIlDtfG9Ph1J5kxEMaZCb/uMlMFMbdqfa9B1Z02XALBZShgVV0hewKEJvacXyewVfglbq6DU3Wd3DkQBO6iX+fkyiDKWm6sMfrP39gLwmnjoF83ZCzBMWFTn0nVIXRnw42s4Cb3vJL8Cn/rzM3+W/2SNVm2JoO9gps5NtuotObKP6E+Kfq47KcVH1dIh2vkwzWKXqxtFlvave2O02Jfv9Jegah7qTJlBM6KKLpK3zwNnX5dly8o2+/XDZDjIJwnnX7dJfK4MgN+jTLnPeZd11JtcO9qqQ5F6gCpUgnOViqT3Xv34mNZT/h1l5Vo7FEa32RFV0X3gHCSvujXOekyuK3lTC2j6uqYARAGlQkTFJ3AHIU7fkyPJ0xQdBX60yD06fv9unH9BAj1hiZ4GEaVh+E4OwTVFWXGBMVRRXf2MrsO3iU4dLderG0U2RMSe0JmTyyybQtsm8R2yGyHO9Ojj54SRH0cKsumyElhatuNiy/m38h31y0zRtGUNkdJpqy5YskEATPTQYnJl5l8kclftkTfinl148sb75wVd+VLlkOy5ZC7edkYOXlxOlkyJsjGhBUdoU+e2erRG5UXgKfqbsZMR9+0T9dLls2Sfous3yLqt6xQyAu7YngA8FAXoAsHSkwsRP0lw77Qcq1lirraeb3T3elhjO4GDxvvjRamyAnZIgtFOdftNy5NH5Cjdsyul6PSJFO6bEr3nnf2XJ1kyp1fL5ny50ckU8HdA5KpSmKqZaZaZKo1Jz97ULLkyZa8b+i5/5o2/0netMbxwCN7qrN0P82zF6zXfWQjUPuj9XSBnfoornQ7Eu7rEit2MfcTzdDeRVekcffTKGhnEtDOKkhCwufRiVX5zOeZ4PR5Pl1NciIJTiJDQFu/C9pZO2oyKSmBA9zNIBwD9qXRO81kUuvPXm1P8k4+WTmU1Dc46hAGHaNJ/lnlklJTU1NKlwwj3QMjY4O9/hHKkgHmHerv6xFgfI8T80u0E8lL1HDf8JJ+TOgHIx41wUhliR3u7x4F6owy55NxZKxnWBiCmc2UsQ8eD+F5n0jBoYyYfgOwBbyt6Ii8U7SlnhobHRMcIwLwk/BiW0um0oHhIWFUmbbpKmgY1PWFiwKcrADfapSXvSDoKIwAjIMTfQH9w4OsJXag+6yD7xNGlNEcHmnhER5mMWBSw7+BiJkN34eNyaMZ6H8m+p+F/mej/zlLRP0S2YTUTUjdhNRNSN2Uo6wpdkUd1V0D+B7Ad3S+QdcswDsAeKmtWHX4KKqDLv/AD4Z7eJimcFjSAWBw9nv2wMAQP9bvyBc4Er4soV/Iw+h7GXr0CGJFrzMdhcyfim7Dr3ScG/94dNFiYPHoYsXA4tGViP/XxaNj3Iyor5R0VbKuStRVrZAGItFD7xP/VMVDx4q+4qE3ioHFQx8UQ8ojj8G6oiOJRD946Ah3wfVSMXK/RB+Q6QMifcCrmhyS6ASZThB9ZYVB/vD7g9Vxxwrhr6amcjMrepqIW9GpYCYISEj4QK9j17vHr8NKPhtc6VpEf8jZifSHGN20x2DzueFX+FQEtxoYLiJ002gQTqDBjQpGnd5JuelfRdrdJrBxHjoKnUX5lGmGF+ldEr1LpneJuMAQHeysuwiWmaH1bsqDgdGjDuh1bsJD2wBwKxrAioCxucmwgHbks65XwSeu0ARxjIBLoCJNEja49l5gdYTRTV7nRGOepNsn6/aJun0rpMmQ9zsdgv8CWAGYzFhR237wGNgVKlT9K6RmQtVwF7gVQxgDCwYujMEIBlMYgxkMEWEMkWCICmNYpyOpFUsYgxUM0WENqKvwBnPEKgZr9CqGpM2rGLZuC2uwwVGtD2tARxXegI4qvAEdVXgDOqrwBnRU4Qwb4KhiQg0PAB4CoA9HwgYCfUNTITOa6EBPnwbTU+Dzr0ITkUCgwYUKRSFyDjRVGCZ2E2h0oUIXYYEPogo7dsLHXoUWYht4qtBE6BjWXXi1+HqxG/+gX0xR6Lu1bNgJn5FiQosemnMXi8ZCiS6S6SJRUzyGdaIuXilTvP8HBjlIBUMcWGb5pxHZBaTuI3JbwU7qoxQC4c+SrYV7dD/bQxbuo34ebzz6nO7nz8Ufs1L3KBowgkH4v45eWeU='))))