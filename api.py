import json
import os
import sys
from datetime import datetime

def handler(request):
    """Vercel Serverless Function Handler"""
    try:
        # パスからルートを判定
        path = request.path
        
        if path == '/api/auth/validate' and request.method == 'POST':
            return validate_auth_handler(request)
        elif path == '/api/health' and request.method == 'GET':
            return health_check_handler()
        elif path == '/api/user/info' and request.method == 'POST':
            return get_user_info_handler(request)
        else:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'Not Found'})
            }
            
    except Exception as e:
        print(f"APIエラー: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Server Error'})
        }

def validate_auth_handler(request):
    """認証トークン検証ハンドラー"""
    try:
        # リクエストボディを取得
        body = request.get_json()
        
        if not body or 'token' not in body:
            return {
                'statusCode': 400,
                'body': json.dumps({
                    'valid': False,
                    'message': 'トークンが提供されていません'
                })
            }
        
        token = body['token'].strip()
        
        if not token:
            return {
                'statusCode': 400,
                'body': json.dumps({
                    'valid': False,
                    'message': 'トークンが空です'
                })
            }
        
        # トークンを検証（簡易版）
        # 実際にはbot2のトークン検証ロジックが必要
        return {
            'statusCode': 200,
            'body': json.dumps({
                'valid': True,
                'user_id': '123456789',
                'user_name': 'Test User',
                'message': '認証成功'
            })
        }
            
    except Exception as e:
        print(f"認証エラー: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'valid': False,
                'message': 'サーバーエラーが発生しました'
            })
        }

def health_check_handler():
    """ヘルスチェックハンドラー"""
    return {
        'statusCode': 200,
        'body': json.dumps({
            'status': 'healthy',
            'timestamp': datetime.now().isoformat()
        })
    }

def get_user_info_handler(request):
    """ユーザー情報取得ハンドラー"""
    try:
        body = request.get_json()
        
        if not body or 'token' not in body:
            return {
                'statusCode': 400,
                'body': json.dumps({
                    'error': 'トークンが提供されていません'
                })
            }
        
        # 簡易版
        return {
            'statusCode': 200,
            'body': json.dumps({
                'user_id': '123456789',
                'user_name': 'Test User',
                'created_at': datetime.now().isoformat(),
                'expires_at': datetime.now().isoformat()
            })
        }
            
    except Exception as e:
        print(f"ユーザー情報取得エラー: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': 'サーバーエラーが発生しました'
            })
        }
