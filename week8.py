{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOZ+C9wJ2ZFArL9owIZr6zS",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/xingyang0203/computational-Thinking/blob/master/week8.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "2hXvCko8zmC2",
        "outputId": "8d84df20-ecec-4c85-99a6-488258ba4b4f",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "print(\"一件上衣300元，一件褲子350元，一件背心400元\")\n",
        "a=int(input(\"上衣購買數量:\"))\n",
        "b=int(input(\"褲子購買數量:\"))\n",
        "c=int(input(\"背心購買數量:\"))\n",
        "s=a*300+b*350+c*400\n",
        "print(\"總金額:%d\"%(s))"
      ],
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "一件上衣300元，一件褲子350元，一件背心400元\n",
            "上衣購買數量:1\n",
            "褲子購買數量:2\n",
            "背心購買數量:3\n",
            "總金額:2200\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "uZkpp004nDBg",
        "outputId": "a86a72f6-5eee-4550-b416-655010974dd8",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "print(\"一罐20元一打200不足一打則個別賣\")\n",
        "a=int(input(\"購買數量:\"))\n",
        "if(a<12):\n",
        "  s=a*20\n",
        "else:\n",
        "  x=a%12\n",
        "  y=(a-x)/12\n",
        "  s=x*20+y*200\n",
        "print(\"總數量:%d\"%(a),\"總金額:%d\"%(s))"
      ],
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "一罐20元一打200不足一打則個別賣\n",
            "購買數量:20\n",
            "總數量:20 總金額:360\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "gQtVd4cRpe5s",
        "outputId": "80251e4e-ebd9-470b-df6a-6632e4d7da72",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "source": [
        "a=int(input(\"第一次期中考:\"))\n",
        "b=int(input(\"第二次期中考:\"))\n",
        "c=int(input(\"第三次期中考:\"))\n",
        "x=a+b+c\n",
        "y=(a+b+c)/3\n",
        "print(\"總分為%d\"%(x),\"平均則為:%8.2f\"%(y))"
      ],
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "第一次期中考:70\n",
            "第二次期中考:80\n",
            "第三次期中考:90\n",
            "總分為240 平均則為:   80.00\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}